import os
import json
from flask import Response, jsonify, request
from app import app
from app.models.user import user
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, unset_jwt_cookies
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


"""
name: manage_session
route: /api/session
paramams: None
methods:
    POST:
        200: Correct Email and password
        404: Correct Email , password do not match
        400: Incorrect email and/or password
    DELETE:
        200: Logout Correct
"""
@app.route("/api/session", methods=["POST", "DELETE"])
def manage_session():
    if request.method == "POST":
        data = request.get_json()
        users, msg = user.validar_login(data)
        if not users:
            return (jsonify(msg)), 400
        elif not bcrypt.check_password_hash(users.password, data["password"]):
            return (jsonify({"password":"Incorrect Password"})), 404
        access_token = create_access_token(identity=users.id)
        refresh_token = create_refresh_token(identity=users.id)
        ans = jsonify(
            {"token": access_token, "id": users.id})
        set_access_cookies(ans, access_token)
        set_refresh_cookies(ans, refresh_token)
        return (ans), 200
    elif request.method == "DELETE":
        ans = jsonify({'logout': True})
        unset_jwt_cookies(ans)
        return (ans), 200

"""
name: register
route: /api/register
paramams: None
methods:
    POST:
        201: User created
        400: Incorrect email and/or password
        500: Internal server error
"""
@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json()
    print(data)
    valid, msg = user.validar(data)
    if not valid:
        return (jsonify(msg)), 400
    pass_hash = bcrypt.generate_password_hash(data['password'])
    data['password'] = pass_hash
    ans = user.save(data)
    if ans is False:
        return (Response(status=500))
    return (Response(status=201))
