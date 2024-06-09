from flask_app import app
from flask import  render_template, request, redirect, session, flash
from flask_app.models.user import User

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'read':
            return redirect("/read")
        elif action == 'create':
            return redirect("/create")
    return render_template("index.html")

@app.route("/read")
def read_all():
    users = User.get_all()
    return render_template("read.html", all_users = users)

@app.route("/create", methods=["POST"])
def create():
    User.save(request.form)
    return redirect("/read")

@app.route("/create")
def create_home():
    return render_template("create.html")

@app.route("/show/<user_id>")
def show(user_id):
    user= User.get_one(user_id)
    return render_template("show.html",user = user)
@app.route("/edit/<user_id>")
def edit(user_id):
    user= User.get_one(user_id)
    return render_template("edit.html",user = user)

@app.route("/update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/read")

@app.route("/delete/<user_id>")
def delete(user_id):
    User.delete(user_id)
    return redirect("/read")