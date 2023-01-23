import os
from app.config.mysqlconnection import connectToMySQL


class general():

    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {cls.modelo} WHERE id = %(id)s"
        data = {'id': id}
        results = connectToMySQL(os.environ.get(
            "DB_NOMBRE")).query_db(query, data)
        return results[0]

    @classmethod
    def validar_existe(cls, campo, valor):
        query = f"SELECT count(*) as contador FROM {cls.modelo} WHERE {campo} = %({campo})s;"
        data = {campo: valor}
        results = connectToMySQL(os.environ.get(
            "DB_NOMBRE")).query_db(query, data)
        return results[0]['contador'] > 0

    @classmethod
    def get_all(cls, rows=None, page=None):
        query = f"SELECT * FROM {cls.modelo};"
        if rows != None and page != None:
            offset = int(rows)*int(page)
            query += f" LIMIT {offset},{int(rows)}"
        results = connectToMySQL(os.environ.get("DB_NOMBRE")).query_db(query)
        return results

    @classmethod
    def get_all_by_condition(cls, campo, valor, rows=None, page=None):
        query = f"SELECT * FROM {cls.modelo} WHERE {campo} = %({campo})s"
        if rows != None and page != None:
            offset = int(rows)*int(page)
            query += f" LIMIT {offset},{int(rows)}"
        data = {campo: valor}
        results = connectToMySQL(os.environ.get(
            "DB_NOMBRE")).query_db(query, data)
        return results

    @classmethod
    def delete(cls, id):
        query = f"DELETE FROM {cls.modelo} WHERE id = %(id)s"
        data = {
            'id': id
        }
        resultado = connectToMySQL(os.environ.get(
            "DB_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def update(cls, data):

        campos_set = ''
        for campo in cls.campos:
            if campo in data:
                if (campo != 'id'):
                    campos_set += campo + '=' + f'%({campo})s,'

        campos_set = campos_set[:-1]

        query = f"""
                UPDATE {cls.modelo} SET {campos_set}
                WHERE id = %(id)s;
                """
        resultado = connectToMySQL(os.environ.get(
            "DB_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado

    @classmethod
    def save(cls, data):

        campos_header = ''
        campos_datos = ''
        for campo in cls.campos:
            campos_header += campo + ','
            campos_datos += f'%({campo})s,'

        campos_header = campos_header[:-1]
        campos_datos = campos_datos[:-1]

        query = f"""
                INSERT INTO {cls.modelo} ({campos_header})
                VALUES ({campos_datos});
                """
        resultado = connectToMySQL(os.environ.get(
            "DB_NOMBRE")).query_db(query, data)
        print("RESULTADO: ", resultado)
        return resultado
