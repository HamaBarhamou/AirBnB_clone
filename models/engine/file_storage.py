#!/usr/bin/python3
"""Recreates a BaseModel from another one by using dictionary rep"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Class that almacenates models of AirBnB clone"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objetcs the obj with key"""
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj.__dict__

    def save(self):
        """Serializes objects to the JSON file"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f, default=str)

    def reload(self):
        """Deserializes the JSON file to __objetcs"""

        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
        except Exception:
            pass

    def update_obejts(self, ob):
        FileStorage.__objects = ob
        self.save()
