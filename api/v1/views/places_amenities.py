#!/usr/bin/python3
""""""

from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.engine.db_storage import classes


@app_views.route("/places/<place_id>/amenities",
                 strict_slashes=False, methods=["GET"])
def get_amenities_place(place_id):
    """"""
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)

    amenities_list = []
    for amenity in place.amenities:
        amenities_list.append(amenity.to_dict())
    return jsonify(amenities_list)


@app_views.route("/places/<place_id>/amenities/<amenity_id>",
                 strict_slashes=False, methods=["DELETE"])
def delete_amenity_place(place_id, amenity_id):
    """"""
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)

    amenity = storage.get(classes["Amenity"], amenity_id)
    if amenity is None:
        abort(404)
    if amenity not in place.amenities:
        abort(404)

    storage.delete(amenity)
    storage.save()
    return jsonify({})


@app_views.route("places/<place_id>/amenities/<amenity_id>",
                 strict_slashes=False, methods=["POST"])
def post_amenity_place(place_id, amenity_id):
    """"""
    place = storage.get(classes["Place"], place_id)
    if place is None:
        abort(404)

    amenity = storage.get(classes["Amenity"], amenity_id)
    if amenity is None:
        abort(404)

    if amenity in place.amenities:
        return jsonify(amenity.to_dict())
    return jsonify(amenity.to_dict()), 201
