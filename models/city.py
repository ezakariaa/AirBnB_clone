#!/usr/bin/python3
"""Defines class City that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a city.

    Attributes:
        state_id (str): id of the state.
        name (str): city's name.
    """

    state_id = ""
    name = ""
