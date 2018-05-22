import hashlib
import os
import sys

from flask import Flask, render_template, request, redirect, session
from model import *
from model import db

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.secret_key = "my-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db.init_app(app)


def redirect_to_login():
    return redirect("/login")


def render_login(purpose="login", error_reason=None):
    return render_template("login.html", reason=error_reason, purpose=purpose)


def string_hash(str):
    return hashlib.md5("whatever your string is".encode('utf-8')).hexdigest()


@app.route("/")
def root():
    if not session.get("logged_in"):
        return redirect_to_login()

    username = session.get('username')
    user = User.query.filter_by(username=username).first()
    user_list = User.query.filter(User.registered_at > user.registered_at).all()

    return render_template('index.html', username=username, user_list=user_list, logged_in=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    is_logged_in = session.get("logged_in")
    if is_logged_in is True:
        return redirect('')

    if request.method == 'GET':
        return render_login()

    if request.method == 'POST' and request.form:
        username = request.form['username']
        password = string_hash(request.form['password'])

        user = User.query.filter_by(username=username).first()
        if user is None:
            return render_login(error_reason="User with username " + username + " doesn't exist")
        if user.password != password:
            return render_login(error_reason="Invalid password")

        session["logged_in"] = True
        session["username"] = username
        return redirect_to_login()

    return render_login()


@app.route("/logout")
def logout():
    if not session['logged_in']:
        return redirect('')
    session["logged_in"] = False
    session.pop("username")
    return redirect_to_login()


def passwords_match(form):
    password = form["password"]
    password_repeat = form["password_repeat"]

    return password == password_repeat


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST' and request.form:
        match = passwords_match(request.form)
        if not match:
            return render_login(purpose="register", error_reason="Passwords must match")

        try:
            form = request.form
            username = form["username"]
            password = string_hash(form["password"])
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect("/login")
        except Exception as e:
            print(e, file=sys.stderr)
            return render_login(purpose="register", error_reason="Username is already taken")

    if session.get('logged_in'):
        return redirect('')
    else:
        return render_login(purpose="register")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)

