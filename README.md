# 57Blocks Backend Test
## Pokemon API DEMO http://64.225.10.215/
### API DOCUMENTATION /app/docs/postman
Pokemon API DEMO FOR 57Blocks Backend test

- User login/validation/identification
- Pokemon Creation/Read/Edit

## Features

- User Creation and validation
- JWT user identification for permissions 
- Pokemon Read Pagination
- Pokemon Read Authorization
- Pokemon Edit Authorization

## Tech

- [Python] - Main language
- [Flask] - Backend Server
- [pytest] - Unit testing
- [MySQL] - Data Base


## Installation

Python 3.9 required
MySQL required


Setup MySQL
```sh
-open and execute  /app/docs/Eschema Scripts.sql query on MySQL workbench
-import data from self contained file /app/docs/db/*.sql on MySQL workbench data import/restore  to 57Blocks DB
```
Install the dependencies and devDependencies and start the server.

```sh
python3 -m pip install pipenv
python3 -m pipenv install
run server.py
```

Unit Testing
```sh
run pytest tests/user_test.py
```

