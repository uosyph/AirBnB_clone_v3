#!/usr/bin/python3
"""API Blueprint for version 1 of the App.

This module initializes the Flask blueprint for version 1 of the API.
It sets the URL prefix for all routes under this version to '/api/v1'.
The blueprint is used to organize and register the various view modules
that handle specific endpoints of the API.
"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
