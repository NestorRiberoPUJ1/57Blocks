import os
from app.config.mysqlconnection import connectToMySQL
from app.utils.regex import REGEX_PASSWORD, REGEX_CORREO_VALIDO
from app.models.general import general

class user(general):

    modelo = 'users'
    campos = ['email', 'password']

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def buscar(cls, dato):
        query = f"select * from {cls.modelo} where id = %(dato)s OR email = %(dato)s"
        data = {'dato': dato}
        results = connectToMySQL(os.environ.get(
            "DB_NOMBRE")).query_db(query, data)

        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def validar(cls, data):

        is_valid = True
        msg = {}

        for campo in cls.campos:
            if not campo in data:
                is_valid = False
                msg[campo] = "Missing Field"
            elif len(str(data[campo])) == 0 or data[campo] == None:
                is_valid = False
                msg[campo] = "Field is required"
            elif campo == "password":
                if len(data[campo]) < 10:
                    is_valid = False
                    msg[campo] = "Password must be at least 10  characters"
                elif not REGEX_PASSWORD.match(data[campo]):
                    is_valid = False
                    msg[campo] = "Password must contain at least: one Upper Case, one lower case, and one of the following special characters @#?]"
            elif campo == "email":
                if not REGEX_CORREO_VALIDO.match(data[campo]):
                    is_valid = False
                    msg[campo] = "Provide a valid Email"
                elif cls.validar_existe("email", data[campo]):
                    is_valid = False
                    msg[campo] = "Email already taken"
        return is_valid, msg

    @classmethod
    def validar_login(cls, data):
        is_valid = True
        msg = {}

        for campo in cls.campos:
            if not campo in data:
                is_valid = False
                msg[campo] = "Missing Field"
            elif len(str(data[campo])) == 0 or data[campo] == None:
                is_valid = False
                msg[campo] = "Field is required"
            elif campo == "password":
                if len(data[campo]) < 10:
                    is_valid = False
                    msg[campo] = "Password must be at least 10  characters"
                elif not REGEX_PASSWORD.match(data[campo]):
                    is_valid = False
                    msg[campo] = "Password must contain at least: one Upper Case, one lower case, and one of the following special characters @#?]"
            elif campo == "email":
                if not REGEX_CORREO_VALIDO.match(data[campo]):
                    is_valid = False
                    msg[campo] = "Provide a valid Email"
                elif not cls.buscar(data[campo]):
                    is_valid = False
                    msg[campo] = "Email not registered"
                else:
                    is_valid = cls.buscar(data[campo])
        return is_valid, msg

