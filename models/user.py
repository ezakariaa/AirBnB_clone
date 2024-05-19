#!/usr/bin/python3
"""Defines class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a User.

    Attributes:
        email (str): User's email.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
