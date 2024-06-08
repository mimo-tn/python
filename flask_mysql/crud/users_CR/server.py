from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'read':
            return redirect("/read")
        elif action == 'create':
            return redirect("/create")
    # users = User.get_all()
    return render_template("index.html")

@app.route("/read")
def read_all():
    users = User.get_all()
    return render_template("read.html", all_users = users)
@app.route("/create", methods=["POST"])
def create():
    # source = request.form.get('source')
    print("helle ")
    print(request.form)
    User.save(request.form)
    return redirect("read")
    # if source == 'page_create':
    #     User.save(request.form)
    #     return redirect("read")
    # elif source == 'page_home':
    #     return render_template("create.html")
    # else:
    #     return render_template("create.html")
@app.route("/create")
def create_home():
    return render_template("create.html")
    
if __name__ == "__main__":
    app.run(debug=True)