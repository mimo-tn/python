from flask_app import app
from flask import render_template, redirect, session, request, url_for
from flask_app.models.book import Book

@app.route('/add/books')
def show_books():
    result= Book.get_all()
    if result:
        return render_template("books.html",books = result)
    else:
        return "books not found", 404  # Or render a template for a 404 page