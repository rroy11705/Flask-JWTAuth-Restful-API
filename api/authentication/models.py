from flask import Flask, jsonify, request, make_response
from passlib.hash import pbkdf2_sha256
import uuid
import jwt
import datetime
from connection import DATABASE


class User:

    def create_user():

        req = request.get_json()

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": req['name'],
            "email": req['email']
        }

        user["password"] = pbkdf2_sha256.using(rounds=8000, salt_size=100).hash(req['password'])

        # Check for existing email address
        if DATABASE.users.find_one({ "email": user['email'] }):
            return make_response(jsonify({ "message": "Email Address Already In Use" }), 400)

        if DATABASE.users.insert_one(user):
            return make_response({'message':'User Created Successfully'}, 200)

        return make_response(jsonify({ "message": "Signup Failed" }), 400)


    def user_login(secret_key):

        req = request.get_json()

        # find user data from db
        user = DATABASE.users.find_one({ "email": req['email'] }, { "password": 1 })

        # check user exist
        if user:

            # check password match
            if pbkdf2_sha256.verify(req['password'], user['password']):

                # create jwt token
                token = jwt.encode(
                    {
                        'email': req['email'],
                        'role': 'user',
                        'iat': datetime.datetime.utcnow(),
                        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)    #token expires after 1 min
                    },
                    secret_key
                )

                DATABASE.users.update_one({ "email": req['email'] }, { "$set": {"token": token } })

                return make_response(jsonify({ 'token': token.decode('UTF-8') }), 201)

            else:
                return make_response(jsonify({ 'message': 'Password is not Correct' }), 400)

        else:
            return make_response(jsonify({ 'message': 'Email Donot Exist' }), 400)

    
    def reset_password():
        req = request.get_json()

        # find user data from db
        user = DATABASE.users.find_one({ "email": req['email'] }, { "password": 1})

        # check user exist
        if user:

            if pbkdf2_sha256.verify(req['password'], user['password']):

                new_password = pbkdf2_sha256.using(rounds=8000, salt_size=100).hash(req['new_password'])

                # update new password
                if DATABASE.users.update_one({ "email": req['email'] }, { "$set": { "password": new_password } }):
                    return make_response(jsonify({ 'message':'Password Updated Successfully' }), 200)

                else:
                    return make_response(jsonify({ "message": "Password Update Failed" }), 400)

            else:
                return make_response(jsonify({ 'message': 'Password is not Correct' }), 400)

        else:
            return make_response(jsonify({ "message": "Email Donot Exist" }), 400)

            
            

