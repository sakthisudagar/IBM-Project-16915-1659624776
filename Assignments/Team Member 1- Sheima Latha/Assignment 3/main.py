from flask import Flask, render_template, request, redirect, url_for
from connect import *
from objstorage import *
app = Flask(__name__)
@app.route('/', methods=('GET','POST'))
@app.route('/registration', methods=('GET','POST'))
def reg_page():
    if request.method == 'POST':
        rollno = request.form['rollno']
        mailid = request.form['mailid']
        username = request.form['username']
        password = request.form['password']
        query = "insert into user values('"+rollno+"','"+mailid+"','"+username+"','"+password+"');"
        ibm_db.exec_immediate(conn,query)
        return redirect(url_for('login_page'))
    return render_template('registration.html')

@app.route('/login', methods=('GET','POST'))
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query = "select COUNT(*) from user where username='"+username+"' and password='"+password+"'"
        stmt1 = ibm_db.exec_immediate(conn,query)
        row = ibm_db.fetch_tuple(stmt1)
        if row[0] == 1:
            return render_template('welcome.html')
    return render_template('login.html')

@app.route('/welcome', methods=('GET','POST'))
def welcome_page():
    return render_template('welcome.html')

@app.route('/redirect_to')
def redirect_to():
    link = request.args.get('link', '/')
    return redirect(link), 301

@app.route('/assign3')
def assign3_page():
    return render_template('assign3img.html')

@app.route('/assign3css')
def assign3css_page():
    return render_template('assign3imgcss.html')

@app.route('/myassistant')
def assistant_page():
    return render_template('assistant.html')

if(__name__=='__main__'):
    app.run()