
import os
import json
from flask import Response, jsonify, request
from app import app
from app.models.pokemon import pokemon
from flask_jwt_extended import jwt_required, get_jwt_identity

"""
name: create_pokemon
route: /api/pokemon
JWT: Required
paramams: None
methods:
    POST:
        201: Pokemon Created
        400: Incorrect data
        500: Internal server error
"""


@app.route("/api/pokemon", methods=["POST"])
@jwt_required()
def create_pokemon():
    data = request.get_json()
    data["user_id"] = get_jwt_identity()
    valid, msg = pokemon.validar(data)
    if not valid:
        return (jsonify(msg)), 400
    ans = pokemon.save(data)
    if ans is False:
        return (Response(status=500))
    return (jsonify({"id": ans})), 201


"""
name: get_pokemon
route: /api/pokemon
JWT: Required
paramams: None
args:
    user: if true, get only users private pokemons
    page: actual page to show
    rows: items pher page to show
methods:
    GET:
        200: Proccess Correct
        401: Unauthorized
        400: Incorrect Args
"""


@app.route("/api/pokemon", methods=["GET"])
@jwt_required()
def get_pokemon():
    args = request.args
    rows = None
    page = None
    if ("rows" in args and "page" in args):
        try:
            rows = int(args["rows"])
            page = int(args["page"])
        except:
            return (Response(status=400))
    if ("user" in args):
        if (str(args["user"]) != "true"):
            return ([]), 401
        pokemons = pokemon.get_all_by_condition(
            "user_id", get_jwt_identity(), rows, page)
    else:
        pokemons = pokemon.get_all_by_condition("public", True, rows, page)
    if not pokemons:
        return ([]), 404
    return (pokemons), 200


"""
name: edit_pokemon
route: /api/pokemon
JWT: Required
paramams: None
args:
    id: id of pokemon to edit
methods:
    PUT:
        200: Pokemon Edited
        400: Incorrect data
        401: Unauthorized
"""


@app.route("/api/pokemon", methods=["PUT"])
@jwt_required()
def edit_pokemon():
    args = request.args
    if ("id" in args):
        data = request.get_json()
        data["id"] = args["id"]
        user_id = get_jwt_identity()
        valid, msg = pokemon.validar_edit(data)
        if not valid:
            return (jsonify(msg)), 400
        poke = pokemon.get_by_id(args["id"])
        if poke["user_id"] != user_id:
            return (Response(status=401))
        ans = pokemon.update(data)
        if ans is False:
            return (Response(status=500))
        poke = pokemon.get_by_id(args["id"])
        return (jsonify(poke)), 200
    else:
        return (Response(status=400))
