#!/usr/bin/env python3
""" Users views module """

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """ Retrieves the list of all User objects """
    all_users = User.all()
    list_users = []

    for user in all_users.values():
        list_users.append(user.to_json())

    return jsonify(list_users)


@app_views.route('/users/me', methods=['GET'],
                 strict_slashes=False)
def get_current_user():
    """ Retrieves the authenticated User object """

    if request.current_user is None:
        abort(404)

    return jsonify(request.current_user.to_json())


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id):
    """ Retrieves one user """

    user = User.get(user_id)

    if user is None:
        abort(404)

    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """ Deletes a user """

    user = User.get(user_id)

    if user is None:
        abort(404)

    user.remove()
    return jsonify({})


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ Creates a User """

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    if "email" not in data:
        return jsonify({"error": "Missing email"}), 400

    if "password" not in data:
        return jsonify({"error": "Missing password"}), 400

    user = User()

    for key, value in data.items():
        setattr(user, key, value)

    user.save()
    return jsonify(user.to_json()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """ Updates a user """

    user = User.get(user_id)

    if user is None:
        abort(404)

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    ignore = ["id", "email", "created_at", "updated_at"]

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)

    user.save()
    return jsonify(user.to_json())
