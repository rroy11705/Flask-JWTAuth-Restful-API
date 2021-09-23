from flask import request, make_response, jsonify, abort
from functools import wraps
from passlib.hash import pbkdf2_sha256
from connection import DATABASE
import jwt


def verify_token(secret_key=None):

    def pre_decorator(f):

        @wraps(f)
        def decorator(*args, **kwargs):

            if not 'Authorization' in request.headers:
                abort(401)

            data = request.headers['Authorization']
            token = str.replace(str(data), 'Bearer ','')
            
            if token is None:
                return make_response(jsonify({ 'message': 'You are missing Token' }), 400)
                
            else:
                try:
                    data = jwt.decode(token, secret_key)
                    print(data)
                    kwargs['email'] = data['email']
                    return f(*args, **kwargs)

                except Exception as e:
                    return make_response(jsonify({ 'message': 'Token has expired' }), 400)
        return decorator
    return pre_decorator
