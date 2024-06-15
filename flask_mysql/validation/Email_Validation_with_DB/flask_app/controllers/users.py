from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.user import User

@app.route('/')
def index():
    result= User.get_all()
    if result:
        return render_template("index.html",users = result)
    else:
        return render_template("users.html")
@app.route('/add/user', methods = ['POST'])
def add_user_form():
    if User.validate_form(request.form):
        User.save(request.form)
        return redirect('/')
    else:
        return redirect('/add_user')
    
@app.route('/add_user')
def add_user():
    return render_template('users.html')
