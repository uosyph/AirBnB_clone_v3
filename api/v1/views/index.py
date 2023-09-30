#!/usr/bin/python3
"""Routes Handling for the App."""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def check_status():
    """Returns the status of the API."""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def objects_count():
    """Retrieves the number of each objects by type."""
    objects = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    objects_dict = {}
    for key, value in objects.items():
        objects_dict[key] = storage.count(value)
    return jsonify(objects_dict)


if __name__ == "__main__":
    pass
