import dbm
import hashlib
import codecs
import sqlite3

from flask import Flask, render_template, request, session, url_for
from werkzeug.utils import redirect, escape


conn = sqlite3.connect("mydatabase.db", check_same_thread = False)
cursor = conn.cursor()


def start_bd():
    # Создание таблицы
    try:
        cursor.execute("""CREATE TABLE users 
                          (user_id, username, password TEXT)
                       """)
        #add_users()
    except sqlite3.OperationalError:
        print("table exist")

def add_users():
    users_list = [(1, 'test1', '123'),
                  (2, 'test2', '123'),
                  (3, 'тест3', '123'),
                  (4, 'тест4', '123'),
                  (5, 'тест5', '123'),
                  (6, 'тест6', '123')]

    cursor.executemany("INSERT INTO users VALUES (?,?,?)", users_list)
    conn.commit()

def print_all_users():
    try:
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        for user in result:
            print(user)
    except sqlite3.OperationalError:
        return

def take_last_id():
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM users ORDER BY user_id")
    result = cursor.fetchall()
    return (len(result))

def create_user(username, password):
    id = take_last_id() + 1
    if isUserExist(username):
        return 1
    sql = "INSERT INTO users VALUES (?,?,?) "
    result = cursor.executemany(sql, [(id, username, password)])
    conn.commit()
    print(result.fetchall())
    return 0

def checkUser(username, password):
    if isUserExist(username):
        sql = "SELECT password FROM users WHERE username=?"
        result = cursor.execute(sql, [username])
        result = result.fetchall()
        if result[0][0] == password:
            return 0
    return 1

def isUserExist(username):
    sql = "SELECT user_id FROM users WHERE username=?"
    # sql = "INSERT INTO users VALUES ('Glow', 'Andy Hunter', '7/24/2012',
    #              'Xplore Records', 'MP3')"
    result = cursor.execute(sql, [username])
    return len(result.fetchall())


def generate_list_by_user(username):
    lst = []
    if isUserExist(username):
        sql = "SELECT user_id FROM users WHERE username=?"
        result = cursor.execute(sql, [username])
        result = result.fetchall()
        sql = "SELECT username FROM users WHERE user_id>?"
        result = cursor.execute(sql, [result[0][0]])
        result = result.fetchall()
        for user in result:
            lst.append(user[0])
            print(user[0])
        return lst
    return lst



app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name1>')
def hello(name1=None):
    return render_template('testhtml.html', name2=name1)


@app.route('/')
def index():
    if 'username' in session:
        user = escape(session['username'])
        #user = user[2:-1]
        #user = user.decode('utf8', errors='ignore')
        lst = generate_list_by_user(user)
        #user = str("b'" + user + "'").encode().decode()
        return render_template('index.html', user=user, list_of_users=lst)
    return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
@app.route('/hello/<error>', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("POST")
        user = request.form['username']
        #user = user.encode('utf8', errors='ignore')
        password = request.form['pass']
        request_type = request.form['act']
        if request_type == "register":
            answer = register_user(user, password)
            if answer == 0:
                return redirect(url_for('index'))
            if answer == 1:
                return render_template('login.html', error="Bad username or password")
            if answer == 2:
                return render_template('login.html', error="This username already used")

        if login_user(user, password) == 0:
            return redirect(url_for('index'))
        return render_template('login.html', error="Bad username or password")

    return render_template('login.html')


def register_user(username, password):
    #password = hash(password)
    #print(password)
    if username == "":
        return 2
    result = create_user(username, password)
    if result != 0:
        return 2
    session['username'] = username
    return 0

def login_user(username, password):
    #password = hash(password)
    result = checkUser(username, password)
    if result == 0:
        session['username'] = username
        return 0
    return result

def hash_pass(password):
    hash = hashlib.md5(password.encode('utf-8')).hexdigest().encode()
    return hash

if __name__ == '__main__':
    start_bd()
    app.secret_key = 'A0Zr98$vwfwfeEFD324LWX/,?RT'
    app.run(host='0.0.0.0')

