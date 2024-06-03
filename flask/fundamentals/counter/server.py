from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'its mw secret key , so keep it secret'

@app.route('/')         
def index():
    if 'count' in session:
        session['count'] += 1 
    else:
        session['count'] = 1
    return render_template("index.html")

# @app.route('/checkout', methods=['POST'])         
# def checkout():
#     print(request.form)
#     count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
#     print(f"charging {request.form['first_name']} for {count} ")
#     return render_template("checkout.html")

@app.route('/destroy_session')         
def destroy_session():
    session.clear()		# clears all keys
    return redirect('/')

@app.route('/add_two')         
def add_two():
    session['count'] += 1
    return redirect('/')

@app.route('/submit_counter', methods=['POST'])         
def submit_counter():
    if 'count' in session:
        session['count'] += (int(request.form['submit_number']) - 1) 
    else:
        session['count'] = (int(request.form['submit_number']) - 1)
    # return render_template("index.html")
    # session['count'] += request.form['submit_number']
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    