from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.post import Post
from flask_app.models.post import User
@app.route('/all_posts')
def read_posts():
    posts = Post.get_all()
    return render_template("wall.html",posts = posts)

@app.route('/post/comment', methods = ['POST'])   
def post_comment():
        if 'first_name' in session:
            session["form"] = "form3"
            if Post.validate_posts(request.form):
                first_data = {"email" : session['email']}
                user = User.get_by_email(first_data)
                second_data = {
                                "user_id" : user.id,
                                "content" : request.form['content']
                            }
                Post.save(second_data)
                return redirect('/all_posts')
        else :
            return redirect('/')
        return redirect('/all_posts')
@app.route('/delete/<int:id>')   
def delete_post(id):
        if 'first_name' in session:
            data ={
                "id" : id
            }
            Post.delete(data)
            return redirect('/all_posts')
        else :
            return redirect('/') 