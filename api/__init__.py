from api.authentication.views import LoginController, SigUpController, ChangePassword
from api.controller.views import Controller
from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)


api.add_resource(LoginController, '/auth/login')
api.add_resource(SigUpController, '/auth/signup')
api.add_resource(ChangePassword, '/auth/reset_password')
api.add_resource(Controller, '/')
