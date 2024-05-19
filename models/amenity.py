#!/usr/bin/python3
"""Defines class Amenity that inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines an amenity.

    Attributes:
        name (str): amenity's name.
    """

    name = ""
