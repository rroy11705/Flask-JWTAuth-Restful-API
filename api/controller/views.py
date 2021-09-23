from flask import app, Flask, request, abort
from flask_restful import Resource, Api, reqparse
import jwt
import os
import json
import datetime
from functools import wraps
from dotenv import load_dotenv, find_dotenv

from decorators.auth_decorators import verify_token


load_dotenv(find_dotenv())

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')


# Controller Class

class Controller(Resource):

    @verify_token(secret_key=app.config['SECRET_KEY'])
    def get(self, *args, **kwargs):
        return f"Hello {kwargs['email']} we are up and working"
