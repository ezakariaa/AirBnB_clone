#!/usr/bin/python3
"""defines BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel.

        Args:
            *args (any): it's not used.
            **kwargs (dict): dictionary of attributes.
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, time_form)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """updates instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns dict containing all keys/values of __dict__ of the instance"""
        returned_dict = self.__dict__.copy()
        returned_dict["created_at"] = self.created_at.isoformat()
        returned_dict["updated_at"] = self.updated_at.isoformat()
        returned_dict["__class__"] = self.__class__.__name__
        return returned_dict

    def __str__(self):
        """returns the str representation of the BaseModel object.

        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
