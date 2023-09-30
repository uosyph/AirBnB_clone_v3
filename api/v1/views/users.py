#!/usr/bin/python3
""""""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.engine.db_storage import classes


@app_views.route("/users", strict_slashes=False, methods=["GET"])
def get_users():
    """"""
    users = storage.all("User")
    users_list = []
    for user in users.values():
        users_list.append(user.to_dict())
    return jsonify(users_list)


@app_views.route("/users/<user_id>", strict_slashes=False, methods=["GET"])
def get_user(user_id):
    """"""
    user = storage.get(classes["User"], user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route("/users/<user_id>", strict_slashes=False, methods=["DELETE"])
def delete_user(user_id):
    """"""
    user = storage.get(classes["User"], user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({})


@app_views.route("/users/", strict_slashes=False, methods=["POST"])
def post_user():
    """"""
    user_data = request.get_json(force=True, silent=True)
    if type(user_data) is not dict:
        abort(400, "Not a JSON")

    if "email" not in user_data:
        abort(400, "Missing email")

    if "password" not in user_data:
        abort(400, "Missing password")
    else:
        new_user = classes["User"](**user_data)
        storage.new(new_user)
        storage.save()
        return jsonify(new_user.to_dict()), 201


@app_views.route("/users/<user_id>", strict_slashes=False, methods=["PUT"])
def put_user(user_id):
    """"""
    user = storage.get(classes["User"], user_id)
    if user is None:
        abort(404)

    user_data = request.get_json(force=True, silent=True)
    if type(user_data) is not dict:
        abort(400, "Not a JSON")

    for key, value in user_data.items():
        if key in ["id", "email", "created_at", "updated_at"]:
            continue
        setattr(user, key, value)

    storage.save()
    return jsonify(user.to_dict())
