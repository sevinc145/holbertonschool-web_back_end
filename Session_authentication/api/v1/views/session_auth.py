#!/usr/bin/env python3
""" Session authentication views """

from os import getenv
from flask import request, jsonify, abort
from models.user import User
from api.v1.views import app_views


@app_views.route('/auth_session/login',
                 methods=['POST'],
                 strict_slashes=False)
def login():
    """ Login user """

    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})

    if len(users) == 0:
        return jsonify(
            {"error": "no user found for this email"}
        ), 404

    user = users[0]

    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())

    response.set_cookie(
        getenv("SESSION_NAME"),
        session_id
    )

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ Logout user """

    from api.v1.app import auth

    if not auth.destroy_session(request):
        abort(404)

    return jsonify({}), 200
