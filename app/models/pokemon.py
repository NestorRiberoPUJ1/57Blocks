import os
from app.config.mysqlconnection import connectToMySQL
from app.models.general import general

class pokemon(general):

    modelo = 'pokemons'
    campos = ['name', 'type', 'health',
              'attack', 'defense', 'public', 'user_id']

    def __init__(self, data):
        self.id = data['id']
        self.type = data['type']
        self.health = data['health']
        self.attack = data['attack']
        self.defense = data['defense']
        self.public = data['public']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def validar(cls, data):

        is_valid = True
        msg = {}
        print(data)

        for campo in cls.campos:
            print(campo)
            if not campo in data:
                is_valid = False
                msg[campo] = "Missing Field"
            elif len(str(data[campo])) == 0 or data[campo] == None:
                is_valid = False
                msg[campo] = "Field is required"
        return is_valid, msg

    @classmethod
    def validar_edit(cls, data):

        is_valid = True
        msg = {}
        print(data)

        for key in data:
            if len(str(data[key])) == 0 or data[key] == None:
                is_valid = False
                msg[key] = "Field is required"

        return is_valid, msg
