from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    db = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data["id"]
        self.dojo_id = data["dojo_id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def save(cls,data):
        query = """
                    INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
                    VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());
                """
        return connectToMySQL(cls.db).query_db(query, data)
    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM ninjas
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)
    @classmethod
    def update(cls, data):
        query = """
                UPDATE ninjas
                SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW()
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)
    @classmethod
    def get_one(cls,data):
        query = """
                    SELECT * FROM ninjas
                    WHERE id = %(id)s;
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])