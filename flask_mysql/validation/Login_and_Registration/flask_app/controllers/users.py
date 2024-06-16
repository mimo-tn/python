from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/register', methods = ['POST'])
def register_form():
    session["form"] = "form1"
    if User.validate_register_form(request.form):
        User.save(request.form)
        session['first_name'] = request.form['first_name']
        return redirect('/login')
    else:
        return redirect('/')
@app.route('/login', methods = ['GET','POST'])   
def login():
    if request.method == 'POST':
        session["form"] = "form2"
        if User.validate_login(request.form):
            data = {"email" : request.form["password_login"]}
            user = User.get_by_email(data)
            session['first_name'] = user.first_name
            return render_template("login.html")
        else :
            return redirect('/')   
    else:
        return render_template("login.html")
@app.route('/destroy_session')         
def destroy_session():
    session.clear()		# clears all keys
    return redirect('/')