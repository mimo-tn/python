from flask_app.config.mysqlconnection import db,connectToMySQL
from flask import flash
from flask_app import app


class Comment:
    def __init__(self, data):
        self.id = data["id"]
        self.user_id = data["user_id"]
        self.recipe_id= data["recommand_id"]
        self.note = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def add_comment(cls , data):
        query = "INSERT comments ( user_id, recommand_id, comment, created_at, updated_at) VALUES (%(user_id)s, %(recommand_id)s, %(comment)s, NOW(), NOW());"
        return connectToMySQL(db).query_db(query , data)
    @classmethod
    def remove_user_like(cls , data):
        query = "DELETE comments WHERE user_id = %(user_id)s AND recommand_id = %(recommand_id)s;"
        return connectToMySQL(db).query_db(query , data)