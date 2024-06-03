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

@app.route('/submit_num', methods=['POST'])         
def submit_counter():
    if 'random_num' in session:
        if session['num_try'] < 5:
            if session['random_num'] == int(request.form['submit_number']):
                if session['num_try'] == 0:
                    session['num_try'] += 1
                session['test'] = f"You Guess it! the number is {session['random_num']} and you took {session['num_try']} attempts "
                session['bg_color'] = "green"
            
            elif session['random_num'] < int(request.form['submit_number']): 
                session['test']  = "Too High!"
                session['bg_color'] = "red"
                session['num_try'] += 1
            else:
                session['test']  = "Too Low!"
                session['bg_color'] = "red" 
                session['num_try'] += 1
        else:
            session['test']  = "You loose!"
            session['bg_color'] = "red" 
    return redirect('/')


@app.route('/destroy_session')         
def destroy_session():

    session.clear()		# clears all keys
    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True)    