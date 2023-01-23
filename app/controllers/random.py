import requests


from flask import Response, jsonify, request
from app import app
from flask_jwt_extended import jwt_required, get_jwt_identity

"""
name: get_rand
route: /api/random
JWT: Required
paramams: None
methods:
    GET:
        200: Correct
        500: Internal server error
"""
@app.route("/api/random", methods=["GET"])
@jwt_required()
def get_rand():
    response = requests.request(
        "GET", "https://www.randomnumberapi.com/api/v1.0/random")
    print(response.text)
    if response.status_code != 200:
        return (), response.status_code
    return (response.text), response.status_code
