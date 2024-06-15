from flask_app.config.mysqlconnection import connectToMySQL,db
from flask_bcrypt import Bcrypt
from flask import flash
from flask_app import app
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO user (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s);
                """
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM user;
                """
        users = connectToMySQL(db).query_db(query)
        if users:
            user = []
            for row in users:
                user.append(cls(row))
            return user
        else:
            return []
    @classmethod
    def get_by_email(cls, data):
        query = """
                SELECT * FROM user
                WHERE email = %(email)s;
                """
        user = connectToMySQL(db).query_db(query, data)
        if user:
            return cls(user[0])
        else:
            return []
    @classmethod
    def edit(cls, data):
        query = """
                UPDATE user
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW()
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM user
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query, data)
    @staticmethod
    def validate_form(data):
        is_valid= True
        email = User.get_by_email(data)
        flash(data['first_name'], 'first_name')
        flash(data['last_name'], 'last_name')
        flash(data['email'], 'email')
        if email:
            is_valid = False
            flash("A user with this email already exists.",'error1')
        if not data["first_name"]:
            is_valid = False
            flash("You must put a first name.",'error2')
        if not data["last_name"]:
            is_valid = False
            flash("You must put a last name.",'error3')
        if not data["email"]:
            is_valid = False
            flash("You must put a email",'error4')
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("invalid Email",'error5')
        return is_valid