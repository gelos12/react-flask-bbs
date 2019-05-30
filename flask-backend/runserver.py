from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)

api = Api(app)

from api_v1 import route

if __name__ == "__main__":
    app.runserver('localhost', 3248, debug=True)