from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.comment import Comment

@app.route('/creat_comment', methods = ['POST'])
def process_input():
    if 'first_name' in session:
        data = {
                "user_id" : request.form['user_id'],
                "recommand_id" : request.form['recommand_id'],
                "comment" : request.form['comment']
                }
        print(f"salalalalalala{data}")
        Comment.add_comment(data)
        return redirect('/all_recommands')
    else :
        return redirect('/')
