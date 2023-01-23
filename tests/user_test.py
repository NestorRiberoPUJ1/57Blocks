import pytest
import os
from flask.testing import FlaskClient
from app import app


@pytest.fixture
def client():
    os.environ["APP_SECRET_KEY"] = "57BlocksTest"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_USER"] = "root"
    os.environ["DB_PASSWORD"] = ""
    os.environ["DB_NOMBRE"] = "57Blocks"
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
