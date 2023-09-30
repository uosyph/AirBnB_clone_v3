# AirBnB clone - RESTful API

The AirBnB clone RESTful API is a Flask web application that provides endpoints for various functionalities related to the AirBnB clone project.

This directory contains the file structure for the AirBnB clone RESTful API.

## File Structure

- [v1](v1/): This directory contains the first version of the API.
  - [app.py](v1/app.py): This file runs the Flask web application.
  - [views](v1/views/): This directory contains all of the views for the Flask web application.
    - [amenities.py](v1/views/amenities.py): This file contains the view for Amenity objects.
    - [cities.py](v1/views/cities.py): This file contains the view for City objects.
    - [index.py](v1/views/index.py): This file contains the view for stats and statuses.
    - [places.py](v1/views/places.py): This file contains the view for Place objects.
    - [place_amenities.py](v1/views/place_amenities.py): This file contains the view for Amenities objects by Place.
    - [place_reviews.py](v1/views/place_reviews.py): This file contains the view for Reviews objects by Place.
    - [states.py](v1/views/states.py): This file contains the view for State objects.
    - [users.py](v1/views/users.py): This file contains the view for User objects.
