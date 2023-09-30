#!/usr/bin/python3
""""""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.engine.db_storage import classes


@app_views.route("/cities/<city_id>/places",
                 strict_slashes=False, methods=["GET"])
def get_places(city_id):
    """"""
    city = storage.get(classes["City"], city_id)
    if city is None:
        abort(404)

    places_list = []
    for place in city.places:
        places_list.append(place.to_dict())
    return jsonify(places_list)


@app_views.route("/places/<place_id>", strict_slashes=False, methods=["GET"])
def get_place(place_id):
    """"""
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("/places/<place_id>",
                 strict_slashes=False, methods=["DELETE"])
def delete_place(place_id):
    """"""
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({})


@app_views.route("/cities/<city_id>/places",
                 strict_slashes=False, methods=["POST"])
def post_place(city_id):
    """"""
    city = storage.get(classes["City"], city_id)
    if city is None:
        abort(404)

    place_data = request.get_json(force=True, silent=True)
    if type(place_data) is not dict:
        abort(400, "Not a JSON")

    if "user_id" not in place_data:
        abort(400, "Missing user_id")

    user_obj = storage.get(classes["User"], place_data["user_id"])
    if user_obj is None:
        abort(404)

    if "name" not in place_data:
        abort(400, "Missing name")
    else:
        new_place = classes["Place"](city_id=city_id, **place_data)
        storage.new(new_place)
        storage.save()
        return jsonify(new_place.to_dict()), 201


@app_views.route("/places_search", strict_slashes=False, methods=["POST"])
def post_place_search():
    """"""
    place_data = request.get_json(force=True, silent=True)
    if type(place_data) is not dict:
        abort(400, "Not a JSON")

    if place_data == {}:
        return storage.all(classes["Place"])


@app_views.route("/places/<place_id>", strict_slashes=False, methods=["PUT"])
def put_place(place_id):
    """"""
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)

    place_data = request.get_json(force=True, silent=True)
    if type(place_data) is not dict:
        abort(400, "Not a JSON")

    for key, value in place_data.items():
        if key in ["id", "user_id", "city_id", "created_at", "updated_at"]:
            continue
        setattr(place, key, value)

    storage.save()
    return jsonify(place.to_dict())
