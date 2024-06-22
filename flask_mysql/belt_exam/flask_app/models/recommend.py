from flask_app.config.mysqlconnection import db,connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.comment import Comment

class Recommand:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.release_date = data["release_date"]
        self.comments = data["comments"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.users_who_comment = []
        self.comment = []
        self.owner = None
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO recommands (title, network, comments, release_date, user_id , created_at, updated_at)
                VALUES (%(title)s, %(network)s, %(comments)s, %(release_date)s, %(user_id)s, NOW(), NOW());
                """
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM recommands
            LEFT JOIN users AS owners ON recommands.user_id = owners.id
            LEFT JOIN comments ON recommands.id =  comments.recommand_id
            LEFT JOIN users AS users_who_comment ON users_who_comment.id = comments.user_id
            ORDER BY recommands.id;
        """
        results = connectToMySQL(db).query_db(query)
        recommands = []
        if results :

            for row in results:
                new_recommand = True
                user_who_comment_data = {
                    'id': row['users_who_comment.id'],
                    'email': row['users_who_comment.email'],
                    'first_name': row['users_who_comment.first_name'],
                    'last_name': row['users_who_comment.last_name'],
                    'password': row['users_who_comment.password'],
                    'created_at': row['users_who_comment.created_at'],
                    'updated_at': row['users_who_comment.updated_at']
                }
                comment_data = {
                    'id': row['comments.id'],
                    'recommand_id': row['recommand_id'],
                    'user_id': row['comments.user_id'],
                    'comment': row['comment'],
                    'created_at': row['comments.created_at'],
                    'updated_at': row['comments.updated_at']
                }
                number_of_recommands = len(recommands)

                if number_of_recommands > 0:
                    previous_recommand = recommands[number_of_recommands - 1]
                    if previous_recommand.id == row['id']:
                        previous_recommand.users_who_comment.append(User(user_who_comment_data))
                        previous_recommand.comment.append(Comment(comment_data))
                        new_recommand = False

                if new_recommand:
                    recommand = cls(row)
                    owner_data = {
                        'id': row['owners.id'],
                        'email': row['email'],
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                        'password': row['password'],
                        'created_at': row['owners.created_at'],
                        'updated_at': row['owners.updated_at']
                    }
                    recommand.owner = User(owner_data)
                    if row['users_who_comment.id']:
                        recommand.users_who_comment.append(User(user_who_comment_data))
                        recommand.comment.append(Comment(comment_data))
                    recommands.append(recommand)

            return recommands
        else:
            return []
    
    @classmethod
    def get_by_user_id(cls, data):
        query = """
                SELECT * FROM recommands
                LEFT JOIN users
                ON recommands.user_id = users.id
                WHERE users.id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        if results:
            recommands = cls(results[0])
            user_data = {
                    "id" : results[0]["users.id"],
                    "first_name" : results[0]["first_name"],
                    "last_name" : results[0]["last_name"],
                    "email" : results[0]["email"],
                    "password" : None,
                    "created_at" : None,
                    "updated_at" : None
                }
            recommands.users = User(user_data)
            return recommands
        else: 
            return []
    @classmethod
    def get_one_with_title(cls, data):
        query = """
                SELECT * FROM recommands
                WHERE title = %(title)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        if results:
            recommands = cls(results[0])
            return recommands
        else: 
            return []
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM recommands
                LEFT JOIN users
                ON recommands.user_id = users.id
                WHERE recommands.id = %(id)s;
                """
        results = connectToMySQL(db).query_db(query,data)
        if results:
            recommands = cls(results[0])
            user_data = {
                    "id" : results[0]["users.id"],
                    "first_name" : results[0]["first_name"],
                    "last_name" : results[0]["last_name"],
                    "email" : results[0]["email"],
                    "password" : None,
                    "created_at" : None,
                    "updated_at" : None
                }
            recommands.users = User(user_data)
            return recommands
        else: 
            return []
    @classmethod
    def update(cls , data):
        query = """
                UPDATE recommands
                SET title = %(title)s, network = %(network)s, comments = %(comments)s, release_date = %(release_date)s, updated_at = NOW()
                WHERE id = %(id)s;"""
        return connectToMySQL(db).query_db(query , data)
    
    @classmethod
    def delete(cls , data):
        query = """
                DELETE FROM recommands
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query , data)
    @staticmethod
    def validate_recommands(data):
        is_valid= True
        if  not data["title"] and not data["network"]  and not data["comments"]:
            is_valid = False
            flash("All fields required",'error16')
        else:
            input_data ={
                "title" : data["title"],
            }
            flash(data['title'], 'title')
            flash(data['network'], 'network')
            flash(data['comments'], 'comments')
            flash(data['release_date'], 'release_date')
            title_in_db = Recommand.get_one_with_title(input_data)
            if title_in_db:
                is_valid = False
                flash("title must be Unique",'error25')
            if len(data["title"]) < 3:
                is_valid = False
                flash("title must be at least 3 characters",'error17')
            if len(data["network"]) < 3:
                is_valid = False
                flash("network must be at least 3 characters",'error18')
            if len (data["comments"]) < 3:
                is_valid = False
                flash("comments must be at least 3 characters",'error19')
        return is_valid

