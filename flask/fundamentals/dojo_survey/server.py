from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'its mw secret key , so keep it secret'
@app.route('/')         
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,100)
        session['num_try'] = 0
    
    print(session['random_num'])
    return render_template("index.html")

@app.route('/process', methods=['POST'])         
def submit_info():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect("/result")

@app.route('/result')         
def result():
    return render_template("result.html")

@app.route('/destroy_session')         
def destroy_session():

    session.clear()		# clears all keys
    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True)    