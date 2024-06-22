from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.user import User
from flask_app.models.recommend import Recommand
@app.route('/')
def index():
    if 'first_name' in session:
        return redirect('/login')
    return render_template("index.html")
@app.route('/register', methods = ['POST'])
def register_form():
    session["form"] = "form1"
    if User.validate_register_form(request.form):
        User.save(request.form)
        data = {"email" : request.form["email"]}
        session['first_name'] = request.form['first_name']
        session['email'] = request.form['email']
        user = User.get_by_email(data)
        session['id']=user.id
        return redirect('/login')
    else:
        return redirect('/')
@app.route('/login', methods = ['GET','POST'])   
def login():
    if request.method == 'POST':
        session["form"] = "form2"
        if User.validate_login(request.form):
            data = {"email" : request.form["email_login"]}
            user = User.get_by_email(data)
            session['first_name'] = user.first_name
            session['id'] = user.id
            session['email'] = request.form['email_login']
            recommand = Recommand.get_all()
            return render_template("recommand.html",recommands = recommand, zip=zip)
        else :
            return redirect('/')   
    else:
        if not 'first_name' in session:
            return redirect('/')
        recommand = Recommand.get_all()
        return render_template("recommand.html",recommands = recommand, zip=zip)
@app.route('/destroy_session')         
def destroy_session():
    session.clear()		# clears all keys
    return redirect('/')