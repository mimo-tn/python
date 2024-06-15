from flask_app.config.mysqlconnection import db, connectToMySQL
from flask_app.models import author
from flask import flash

class Book:
    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at =  data["updated_at"]
        self.authors = []
    @classmethod
    def save(cls,data):
        query=  """
                INSERT INTO books (title, num_od_pages, created_at, updated_at)
                VALUES (%(title)s, %(num_od_pages)s, NOW(), NOW())
                """
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM books;
                """
        return connectToMySQL(db).query_db(query)
    @classmethod
    def get_books_with_authors(cls,data):
        query = """
                SELECT * FROM books
                LEFT JOIN favorits ON books.id = favorits.book_id
                LEFT JOIN authors ON authors.id = favorits.author_id
                WHERE books.id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query, data)
        book = cls(results[0])
        for row in results:
            author_favorits = {
                "id" : row["authors.id"],
                "name" : row["name"],
                "created_at" : None,
                "updated_at" : None
            }
            book.users.append(author.Author(author_favorits))
        return book

        
    
