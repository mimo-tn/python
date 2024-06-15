from flask_app.config.mysqlconnection import connectToMySQL,db
from flask import flash
from flask_app import app
import re


class Order:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.cookie_type = data["cookie_type"]
        self.number_of_boxes = data["number_of_boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def save(cls,data):
        query = """
                INSERT INTO orders (name, cookie_type, number_of_boxes)
                VALUES (%(name)s, %(cookie_type)s, %(number_of_boxes)s);
                """
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM orders;
                """
        orders = connectToMySQL(db).query_db(query)
        if orders:
            order = []
            for row in orders:
                order.append(cls(row))
            return order
        else:
            return []
    @classmethod
    def get_by_id(cls, data):
        query = """
                SELECT * FROM orders
                WHERE id = %(id)s;
                """
        orders = connectToMySQL(db).query_db(query, data)
        if orders:
            return cls(orders[0])
        else:
            return []
    @classmethod
    def edit(cls, data):
        query = """
                UPDATE orders
                SET name = %(name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s, updated_at = NOW()
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM orders
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query, data)
    @staticmethod
    def validate_form(data):
        is_valid= True
        # number_of_boxes = Order.get_by_number_of_boxes(data)
        if not data['name'] and not data['cookie_type'] and not data['number_of_boxes']:
            is_valid = False
            flash("All fields are required",'error1')
        else:
            if not data["name"]:
                is_valid = False
                flash("name is required",'error2')
            elif len(data["name"]) < 2:
                is_valid = False
                flash("name must be at least 2 characters",'error3')

            if not data["cookie_type"]:
                is_valid = False
                flash("cookie type is required",'error4')
            elif len(data["cookie_type"]) < 2:
                is_valid = False
                flash("cookie type must be at least 2 characters",'error5')

            if not data["number_of_boxes"]:
                is_valid = False
                flash("number of boxes is required",'error6')
            elif int(data["number_of_boxes"]) <= 0:
                is_valid = False
                flash("number of boxes must be a positive number",'error7')
        return is_valid