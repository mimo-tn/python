from flask_app import app
from flask import render_template,redirect,session,request,url_for
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
@app.route('/')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html",dojos = dojos)

@app.route('/dojo/new', methods=["POST"])
def new_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/ninja/new')
def add_ninja():
    dojos = Dojo.get_all()
    return render_template("ninja.html",dojos = dojos)

@app.route('/save/ninja', methods=['POST'])
def save_ninja():
    Ninja.save(request.form)
    print(request.form['dojo_id'])
    return redirect(url_for('show', dojo_id=request.form['dojo_id']))

@app.route('/show/<dojo_id>')
def show(dojo_id):
    result = Dojo.get_dojo_with_ninjas(dojo_id)
    if result:
        return render_template("show.html",result = result)
    else :
        return "Dojo not found", 404  # Or render a template for a 404 page
    

