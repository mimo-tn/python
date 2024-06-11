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
    data = {"dojo_id": dojo_id}
    result = Dojo.get_dojo_with_ninjas(data)
    if result:
        return render_template("show.html",result = result)
    else :
        return "Dojo not found", 404  # Or render a template for a 404 page
    
@app.route('/dojo/<int:dojo_id>/ninja/<int:ninja_id>/delete')
def delete(dojo_id,ninja_id):
    data={'id':ninja_id}
    Ninja.delete(data)
    return redirect(f'/show/{dojo_id}')

@app.route('/ninja/<int:ninja_id>/update')
def update(ninja_id):
    data={'id':ninja_id}
    result = Ninja.get_one(data)
    return render_template("update.html",ninja = result)

@app.route('/update/ninja', methods = ["POST"])
def update_form():
    # data={'id':request.form["id"]}
    Ninja.update(request.form)
    dojo_id = request.form["dojo_id"]
    print(f"je suis la {dojo_id}")
    return redirect(f'/show/{dojo_id}')