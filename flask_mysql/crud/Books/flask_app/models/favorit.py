from flask_app.config.mysqlconnection import db, connectToMySQL

class Favorit:
    def __init__(self,data):
        self.author_id = data["author_id"]
        self.book_id = data["book_id"]
    @classmethod
    def save(cls,data):
        query=  """
                INSERT INTO favorits (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s)
                """
        return connectToMySQL(db).query_db(query, data)