#!/usr/bin/python3
"""Defines class State that inherits from BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """Defines a state.

    Attributes:
        name (str): State's name.
    """

    name = ""
