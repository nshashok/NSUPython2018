import time
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine('sqlite:///users.db', echo=True)

app = Flask(__name__)
@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        Session = sessionmaker(bind=engine)
        s = Session()
        usernames = list(s.execute("SELECT username FROM users WHERE id>:param", {"param":session['datetime']}))

        if len(usernames) == 0: usernames.append(("You're the last registered user",))

        return render_template('index.html', username=session['username'], usernames=usernames)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if not session.get('logged_in'):
            return render_template('login.html', correct=True)
        else:
            return redirect('')
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter_by(username=POST_USERNAME)
        result = query.first()
        global corr
        if result:
            if result.check_password(POST_PASSWORD):
                session['logged_in'] = True
                session['username'] = POST_USERNAME
                session['datetime'] = result.id
                return redirect('')
            else:
                return render_template('login.html', correct=False)
        else:
            return render_template('login.html', correct=False)

@app.route("/logout", methods=['GET','POST'])
def logout():
    session['logged_in'] = False
    session['username'] = None
    session['datetime'] = None
    return redirect('')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        if not session.get('logged_in'):
            return render_template('register.html', correct=True)
        else:
            return redirect('')
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter_by(username=POST_USERNAME)
        result = query.first()
        if result:
            return render_template('register.html', correct=False)
        else:
            user = User(POST_USERNAME, POST_PASSWORD)
            s.add(user)
            s.commit()
            session['logged_in'] = True
            session['username'] = user.username
            session['datetime'] = user.id
            return redirect('')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=3000)
