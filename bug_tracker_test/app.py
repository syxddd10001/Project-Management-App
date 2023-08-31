import sys
import re

import mysql.connector
from flask import (Flask, 
                   render_template, 
                   request, 
                   redirect, 
                   url_for, 
                   session)
from flask_mysqldb import MySQL

sys.path.append('model')
import users
import projects
import bugs

#pass_inp = input('db passwd: ')

AUTHENTICATION = False
logged_user = None
blacklist = ['--','"',"'", ';']
regex_email = re.compile('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}')
regex_github = re.compile('https://github.com/[A-Za-z0-9.-_]')
error = ''
app = Flask(__name__)
app.secret_key = 'hGmX2L!0lxfoldxadfsfdonbgu313dxfhnsqwlg'

conn = mysql.connector.connect(
        host='localhost',
        user='syxddd',
        password='securepassword!',
        database = 'bugbase'
    )
print("Connection Successful")
conn.autocommit = True
cursor = conn.cursor(buffered=True)

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'syxddd'
app.config['MYSQL_PASSWORD'] = 'popcornPOP!001'
app.config['MYSQL_DB'] = 'bugbase'

mysql = MySQL(app)
@app.route('/',methods=['GET','POST'])
def index():
    if not logged_user:
        return redirect(url_for('login'))
    else: 
        return redirect(url_for('home'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)
        if (login(cursor)):
            return redirect(url_for('home'))
        
        else:  
            return render_template('login.html', error_statement=error)

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():     
    if request.method == "POST":
        if (signup(cursor)):
            return redirect(url_for('login'))

        else:
            return render_template('signup.html', error_statement=error) 
    
    return render_template('signup.html')

@app.route('/home', methods=['POST','GET'])
def home():  
    if logged_user!=None:            
        success(cursor, logged_user)
        return render_template('home.html', user_name=logged_user.get_username(), data=success(cursor, logged_user))    
        
    else: 
        print('error')
        return redirect(url_for('login'))
        
    

def success(cursor, user):
    global error
    if user == None:
        error = "no user logged in"
        return
    res = user.read_projects(cursor)
    
    return res

@app.route('/logout')
def logout():
    global logged_user
    session.pop('user_id', None)
    logged_user = None
    return redirect(url_for('index'))

def login(cursor):   
    user = request.form['username']
    passw = request.form['password']
    global error
    for i in blacklist:
        if i in user or i in passw:
            error = 'Invalid characters in username or password'
            return
    # checking if user and password combo are correct
    cursor.execute("SELECT username From User WHERE User.username = '%s' AND User.password = '%s'" % (user,passw))
    fetch_data = cursor.fetchone()
    if fetch_data == None:
        error = "Username or password does not exist"
        return 
    #if the combo is correct, fetch all user data
    cursor.execute("SELECT * From User WHERE User.username = '%s'" % user)
    fetch_data = cursor.fetchone()
    
    global logged_user
    logged_user = users.User(fetch_data[0],fetch_data[1],fetch_data[2], fetch_data[3], fetch_data[4])
    
    global session
    if logged_user  is not None:
        session['user_id'] = logged_user.get_username()
    
    conn.commit()
    return True
        
    
def signup(cursor):
    # username check
    global error
    user = request.form['username']
    for i in blacklist:
        if i in user:
            error = 'Bad username'
            return
    
    cursor.execute("SELECT username From User WHERE User.username = '%s'" % user)
    if (cursor.fetchone()):
        error = 'Username already exists'
        return False
    
   # email check
    email = request.form["email"]
    if (not regex_email.findall(email)):
        error = "Invalid email"
        return
        
    cursor.execute("SELECT email From User WHERE User.email = '%s'" % email)
    if (cursor.fetchone()):
        error = 'Email already exists'
        return False
    
    #github check
    github = request.form["github"]
    if not regex_github.findall(github) and len(github) != 0:
        error = 'Invalid Github'
        return
    cursor.execute("SELECT github From User WHERE User.github = '%s'" % github)
    if (cursor.fetchone() and len(github) != 0):
        error = 'GitHub already linked to another account'
        return False
    
    passw = request.form["password"]
    if (len(passw) < 6):
        error = "Password is too short"
        return False

    try:
        print("executed")
        cursor.execute("""
        INSERT INTO User(username, email, github, password)
        VALUES (
            '%s',
            '%s',
            '%s',
            '%s'  
        );""" % (user, email, github, passw,))
        conn.commit() 
        return True
    
    except Exception as e:
        error = e
        return False


def create_project(cursor):
    if logged_user == None:
        return

    print("Add Project: ")
    name=input("Name: ")
    github=input("github.com/")
    description=input("Description: ")
    logged_user.add_project(cursor, name, github, description)



if __name__ == '__main__':
    
    app.secret_key = 'hGmX2L!0lxfoldxadfsfdonbgu313dxfhnsqwlg'
    
    app.run(debug=True)
    conn.commit()

