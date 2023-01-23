from app import app
from flask_cors import CORS

cors = CORS(app,supports_credentials=True)


if __name__ == "__main__":
    app.run(debug=True)
