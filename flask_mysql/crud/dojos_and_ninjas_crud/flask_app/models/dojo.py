from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas =[]
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    @classmethod 
    def save(cls, data):
        query = """
                    INSERT INTO dojos (name, created_at, updated_at)
                    VALUES (%(name)s, NOW(), NOW());
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_dojo_with_ninjas(cls, dojo_id):
        query = """
                SELECT dojos.id AS dojo_id, dojos.name AS dojo_name, ninjas.id AS ninja_id, ninjas.first_name , ninjas.last_name, ninjas.age 
                FROM dojos
                LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
                WHERE dojos.id = %(dojo_id)s;
                """
        results = connectToMySQL(cls.db).query_db(query, {"dojo_id": dojo_id})
        dojo_data = {
            "id": results[0]["dojo_id"],
            "name": results[0]["dojo_name"],
            "created_at": None,  # Adjust as needed
            "updated_at": None   # Adjust as needed
        }
        dojos = cls(dojo_data)
        for row_ninja in results:
            if row_ninja["ninja_id"]:
                ninja_data = {
                        "id": row_ninja["ninja_id"],
                        "dojo_id" : row_ninja["dojo_id"],
                        "first_name": row_ninja["first_name"],
                        "last_name": row_ninja["last_name"],
                        "age": row_ninja["age"],
                        "created_at": None,  # Adjust as needed
                        "updated_at": None   # Adjust as needed
                    }
                dojos.ninjas.append(ninja.Ninja(ninja_data))
        print(dojos.ninjas[0].last_name)
        return dojos


# dojos.ninjas.append(ninja.Ninja(ninja_data))