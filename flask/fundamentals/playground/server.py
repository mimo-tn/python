from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play_1():
    return render_template("play.html", num = 3, color = "aquamarine")
@app.route('/play/<int:num>')
def play_2(num):
    return render_template("play.html", num = num, color = "aquamarine")

@app.route('/play/<int:num>/<string:couleur>')
def play_3(num,couleur):
    return render_template("play.html", num = num, color = couleur)


if __name__ =="__main__":
    app.run(debug=True)
