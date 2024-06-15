from flask_app.config.mysqlconnection import db, connectToMySQL
from flask_app.models import book
class Author:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at =  data["updated_at"]
        self.books = []
    @classmethod
    def save(cls,data):
        query=  """
                INSERT INTO authors (name, created_at, updated_at)
                VALUES (%(name)s, NOW(), NOW())
                """
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM authors;
                """
        return connectToMySQL(db).query_db(query)
    @classmethod
    def get_authors_with_books(cls,data):
        query = """
                SELECT * FROM authors
                LEFT JOIN favorits ON authors.id = favorits.author_id
                LEFT JOIN books ON books.id = favorits.book_id
                WHERE authors.id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query, data)
        author = cls(results[0])
        for row in results:
            book_favorits = {
                "id" : row["books.id"],
                "title" : row["title"],
                "num_of_pages" : row["num_of_pages"],
                "created_at" : None,
                "updated_at" : None
            }
            author.books.append(book.Book(book_favorits))
        return author