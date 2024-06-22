from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.recommend import Recommand
from flask_app.models.recommend import User
@app.route('/all_recommands')
def read_recommands():
    recommand = Recommand.get_all()
    return render_template("recommand.html",recommands = recommand,  zip=zip)

@app.route('/recommands/<int:id>')
def read_one_recommand(id):
    if 'first_name' in session:
        if id :
            data = {"id" : id}
            recommand = Recommand.get_by_id(data)
            return render_template("show_recommand.html", recommand = recommand)
    else:
        return redirect('/')

@app.route('/recommands/new')
def new_recommands_form():
    if 'first_name' in session:
        return render_template("create_recommand.html")
    else:
        return redirect('/')
@app.route('/edit/recommands/<int:id>')
def edit_one_recommand(id):
    if 'first_name' in session:
        if id :
            data = {"id" : id}
            recommand = Recommand.get_by_id(data)
            return render_template("edit_recommand.html", recommand = recommand)
    else:
        return redirect('/')
@app.route('/create/recommands/new', methods = ['POST'])   
def create_recommands():
            if 'first_name' in session:
                session["form"] = "form3"
                if Recommand.validate_recommands(request.form):
                    first_data = {"email" : session['email']}
                    user = User.get_by_email(first_data)
                    second_data = {
                                    "user_id" : user.id,
                                    "title" : request.form['title'],
                                    "network" : request.form['network'],
                                    "comments" : request.form['comments'],
                                    "release_date" : request.form['release_date'],
                                }
                    Recommand.save(second_data)
                    return redirect('/all_recommands')
                return redirect('/recommands/new')
            else :
                return redirect('/')
@app.route('/update/recommands', methods = ['POST'])   
def update_recommands():
            if 'first_name' in session:
                session["form"] = "form4"
                if Recommand.validate_recommands(request.form):
                    data = {
                                    "id" : request.form['id'],
                                    "user_id" : request.form['user_id'],
                                    "title" : request.form['title'],
                                    "network" : request.form['network'],
                                    "comments" : request.form['comments'],
                                    "release_date" : request.form['release_date']
                                }
                    Recommand.update(data)
                    return redirect('/all_recommands')
                recommand = Recommand.get_by_id(request.form)
                return render_template("edit_recommand.html", recommand = recommand)
            else :
                return redirect('/')
@app.route('/delete/<int:id>')   
def delete_post(id):
        if 'first_name' in session:
            data ={
                "id" : id
            }
            Recommand.delete(data)
            return redirect('/all_recommands')
        else :
            return redirect('/') 