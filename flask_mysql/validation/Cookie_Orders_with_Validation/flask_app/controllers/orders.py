from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.order import Order

@app.route('/')
def index():
    result = Order.get_all()
    if result:
        return render_template("index.html",orders = result)
    else:
        return render_template("orders.html")
@app.route('/add/order', methods = ['POST'])
def add_order_form():
    if Order.validate_form(request.form):
        Order.save(request.form)
        return redirect('/')
    else:
        return redirect('/add_order')
@app.route('/update/order', methods = ['POST'])
def edit_order_form():
    if Order.validate_form(request.form):
        Order.edit(request.form)
        return redirect('/')
    else:
        return redirect(url_for('edit_order', id=int(request.form['id'])))
    
@app.route('/cookie/edit/<int:id>')
def edit_order(id):
    data = {'id':id}
    result = Order.get_by_id(data)
    return render_template('update.html',order = result)   

@app.route('/add_order')
def add_order():
    return render_template('orders.html')

