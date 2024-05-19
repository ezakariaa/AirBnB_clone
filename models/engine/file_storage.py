#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file and deserializes it.

    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        nameoc = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(nameoc, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dict_ob = FileStorage.__objects
        di_obj = {obj: dict_ob[obj].to_dict() for obj in dict_ob.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(di_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                di_obj = json.load(f)
                for ob in di_obj.values():
                    name_cls = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(name_cls)(**ob))
        except FileNotFoundError:
            return
