from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.book import Book
from flask_app.models.author import Author
from flask_app.models.favorit import Favorit

@app.route('/')
def index():
    authors_results = Author.get_all()
    return render_template("index.html",authors = authors_results)
@app.route('/save/author', methods=["POST"])
def save_author():
    data = {
        'name' : request.form['name']
    }
    Author.save(data)
    return redirect('/')

@app.route('/author/<int:id>')
def author(id):
    data = {"id": id}
    result = Author.get_authors_with_books(data)
    all_books = Book.get_all()
    if result:
        return render_template("author_show.html",result = result,all_books = all_books)
    else :
        return "Favorits book not found", 404  # Or render a template for a 404 page

@app.route('/save/favorite/book', methods=["POST"])
def save_authors_favorit():
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']

    }
    Favorit.save(data)
    return redirect(url_for('author', id=request.form['author_id']))