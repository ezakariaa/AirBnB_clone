#!/usr/bin/python3
"""Defines class Place that inherits from BaseModel."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defines a place.

    Attributes:
        city_id (str): the id of the city.
        user_id (str): the id of the user.
        name (str): place's name.
        description (str): place's desc.
        number_rooms (int): rooms' num.
        number_bathrooms (int): bathrooms' num.
        max_guest (int): guests max num.
        price_by_night (int): place's price at night.
        latitude (float): latitude of the place.
        longitude (float): longitude of the place.
        amenity_ids (list): list of Amenity.id.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
