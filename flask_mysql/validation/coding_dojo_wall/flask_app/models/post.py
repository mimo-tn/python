from flask_app.config.mysqlconnection import db,connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.user import User

class Post:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users = []
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO posts (content,user_id ,created_at, updated_at)
                VALUES (%(content)s, %(user_id)s, NOW(), NOW());
                """
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM posts
                LEFT JOIN users
                ON posts.user_id = users.id
                ORDER BY posts.created_at DESC;
                """
        results = connectToMySQL(db).query_db(query)
        if results:
            posts = []
            for row in results:
                post = cls(row)
                user_data = {
                    "id" : row["users.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"],
                    "email" : row["email"],
                    "password" : None,
                    "created_at" : None,
                    "updated_at" : None
                }
                post.users = User(user_data)
                posts.append(post)
            return posts
        else: 
            return []
    @classmethod
    def get_by_user_id(cls, data):
        query = """
                SELECT * FROM posts
                LEFT JOIN users
                ON posts.user_id = users.id
                WHERE user.id = %()s;
                """
        results = connectToMySQL(db).query_db(query)
        if results:
            posts = cls(results[0])
            for row in results:
                user_data = {
                    "id" : row["user.id"],
                    "first_name" : row["first_name"],
                    "last_name" : row["last_name"]
                }
                posts.append(User(user_data))
            return posts
        else: 
            return []
    @classmethod
    def update(cls , data):
        query = """
                UPDATE posts
                SET content = %(title)s , updated_at = NOW()
                WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query , data)
    
    @classmethod
    def delete(cls , data):
        query = """
                DELETE FROM posts
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query , data)
    @staticmethod
    def validate_posts(data):
        is_valid= True
        if not data["content"]:
            is_valid = False
            flash("Post content must not be Blank",'error15')
        return is_valid

