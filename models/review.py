#!/usr/bin/python3
"""Defines class Review that inherits from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a review.

    Attributes:
        place_id (str): id's place.
        user_id (str): user's id.
        text (str): review's text.
    """

    place_id = ""
    user_id = ""
    text = ""
