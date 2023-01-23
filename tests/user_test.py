import pytest
import os
from flask.testing import FlaskClient
from app import app
from datetime import timedelta


@pytest.fixture
def client():
    os.environ["APP_SECRET_KEY"] = "57BlocksTest"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_USER"] = "root"
    os.environ["DB_PASSWORD"] = ""
    os.environ["DB_NOMBRE"] = "57Blocks"
    app.config["JWT_SECRET_KEY"] = os.environ.get("APP_SECRET_KEY")
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=20)
    return app.test_client()


def test_register(client: FlaskClient):
    wrongEmail = "Provide a valid Email"
    takenEmail = "Email already taken"
    missingField = "Missing Field"
    requiredField = "Field is required"
    shortPassword = "Password must be at least 10  characters"
    wrongPassword = "Password must contain at least: one Upper Case, one lower case, and one of the following special characters @#?]"

    cases = [
        [
            {},
            {"status_code": 400, "response": {
                "email:": missingField, "password": missingField}}
        ],
        [
            {"email": "", "password": ""},
            {"status_code": 400, "response": {
                "email:": requiredField, "password": requiredField, }}
        ],
        [
            {"email": "test.com", "password": "password"},
            {"status_code": 400, "response": {
                "email:": wrongEmail, "password": shortPassword, }}
        ],
        [
            {"email": "test.com", "password": "password1234"},
            {"status_code": 400, "response": {
                "email:": wrongEmail, "password": wrongPassword, }}
        ],
        [
            {"email": "test@test.com", "password": "Password1234"},
            {"status_code": 400, "response": {
             "password": wrongPassword, }}
        ],
        [
            {"email": "test@test.com", "password": "Password1234#"},
            {"status_code": 201, "response": {}}
        ],
        [
            {"email": "test@test.com", "password": "Password1234!"},
            {"status_code": 400, "response": {"email:": takenEmail}}
        ]
    ]

    for case in cases:
        resp = client.post(
            '/api/register', json=case[0])

        assert resp.status_code == case[1]["status_code"]
        if ("email" in case[1]["response"]):
            assert resp.json.get("email") == case[1]["response"]["email"]
        if ("password" in case[1]["response"]):
            assert resp.json.get("password") == case[1]["response"]["password"]


def test_login(client: FlaskClient):

    wrongEmail = "Provide a valid Email"
    takenEmail = "Email already taken"
    missingField = "Missing Field"
    requiredField = "Field is required"
    shortPassword = "Password must be at least 10  characters"
    wrongPassword = "Password must contain at least: one Upper Case, one lower case, and one of the following special characters @#?]"
    unregisteredEmail = "Email not registered"
    incorrectPassword = "Incorrect Password"

    cases = [
        [
            {},
            {"status_code": 400, "response": {
                "email:": missingField, "password": missingField}}
        ],
        [
            {"email": "", "password": ""},
            {"status_code": 400, "response": {
                "email:": requiredField, "password": requiredField, }}
        ],
        [
            {"email": "test.com", "password": "password"},
            {"status_code": 400, "response": {
                "email:": wrongEmail, "password": shortPassword, }}
        ],
        [
            {"email": "test.com", "password": "password1234"},
            {"status_code": 400, "response": {
                "email:": wrongEmail, "password": wrongPassword, }}
        ],
        [
            {"email": "testo@test.com", "password": "Password1234"},
            {"status_code": 400, "response": {
                "email": unregisteredEmail, "password": wrongPassword, }}
        ],
        [
            {"email": "test@test.com", "password": "Password1234!"},
            {"status_code": 404, "response": {
                "password": incorrectPassword
            }}
        ],
        [
            {"email": "test@test.com", "password": "Password1234#"},
            {"status_code": 200, "response": {}}
        ]
    ]
    for case in cases:

        resp = client.post(
            '/api/session', json=case[0])
        print("CASE: ", case)
        print("RESP: ", resp.json)
        assert resp.status_code == case[1]["status_code"]
        if ("email" in case[1]["response"]):
            assert resp.json.get("email") == case[1]["response"]["email"]
        if ("password" in case[1]["response"]):
            assert resp.json.get("password") == case[1]["response"]["password"]


def test_pokemon(client: FlaskClient):
    resp = client.post(
        '/api/pokemon', json={
            "attack": 10,
            "defense": 70,
            "health": 60,
            "name": "thundra",
            "public": True,
            "type": "Fire"
        })
    assert resp.status_code == 401

    client.post("/api/session",
                json={"email": "test@test.com", "password": "Password1234#"},)
    resp = client.post(
        '/api/pokemon', json={
            "attack": 10,
            "defense": 70,
            "health": 60,
            "name": "thundra",
            "public": True,
            "type": "Fire"
        })
    assert resp.status_code == 201
    created_id = resp.json.get("id")

    resp = client.get('/api/pokemon')
    assert resp.status_code == 200

    resp = client.get('/api/pokemon?user=true')
    assert resp.status_code == 200

    resp = client.get('/api/pokemon?rows=5&page=0')
    assert resp.status_code == 200

    resp = client.post(
        '/api/pokemon?id=1', json={
            "attack": 10,
        })
    assert resp.status_code == 401

    resp = client.put(
        '/api/pokemon?id='+created_id, json={
            "attack": 20,
        })
    assert resp.status_code == 200
