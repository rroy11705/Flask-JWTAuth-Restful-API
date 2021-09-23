from flask import app, Flask, request, jsonify, make_response
from flask_restful import Resource, Api, reqparse
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv, find_dotenv

from .models import User


load_dotenv(find_dotenv())

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

limiter  =  Limiter(
                    app, 
                    key_func=get_remote_address, 
                    default_limits=["200/day","25/hour"]
            )


class LoginController(Resource):
      
    @limiter.limit("10/minute")
    def post(self):
        return User.user_login(app.config['SECRET_KEY'])
        


class SigUpController(Resource):

    @limiter.limit("5/minute")
    def post(self):
        return User.create_user()


class ChangePassword(Resource):

    @limiter.limit("5/minute")
    def put(self):
        return User.reset_password()


@app.errorhandler(429)
def ratelimit_handler(e):
  return make_response(jsonify({ 'message': "You have exceeded your rate-limit" }), 400)