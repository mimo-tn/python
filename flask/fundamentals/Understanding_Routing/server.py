from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def name(name):
    return f"Hi {name}!"

@app.route('/repeat/<string:variable>/<int:numbers>')
def repeat(variable,numbers):
    return f"{variable * numbers}"

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."


if __name__ == "__main__":
    app.run(debug=True)
