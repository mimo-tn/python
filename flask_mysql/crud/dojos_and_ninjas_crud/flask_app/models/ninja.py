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
    #     query = """
    #             select * from dojos
    #             LEFT JOIN ninjas
    #             ON dojos.id = ninjas.dojo_id
    #             WHERE dojos.id = %(dojo_id)s; 
    #             """
    #     results = connectToMySQL(cls.db).query_db(query, {"dojo_id", dojo_id}) 
    #     ninjas = cls(results[0])
    #     for ninja in results:
    #         ninja_data = {
    #             "id" = data["id"]
    #             "dojo_id" = data["dojo_id"]
    #             "first_name" = data["first_name"]
    #             "last_name" = data["last_name"]
    #             "age" = data["age"]
    #             "created_at" = data["created_at"]
    #             "updated_at" = data["updated_at"]
    #         }
    #         ninjas.append(cls(ninja))
