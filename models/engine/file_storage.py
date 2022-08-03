#!/usr/bin/python3
"""Recreates a BaseModel from another one by using dictionary rep"""

import json


class FileStorage:
    """Class that almacenates models of AirBnB clone"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects
    
    def new(self,obj):
        """Sets in __objetcs the obj with key"""
        self.__object["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        with open(self.__file_path, "w", encoding="uft-8") as f:
            for key, value in self.__objects.items():
                #dic_obj[key] = value.to._dict()
                self.__object[key] = value.to._dict()
                #json.dump(dic_obj, f)
                json.dump(self.__object, f)

    def reload(self):
        """Deserializes the JSON file to __objetcs"""

        try:
            with open(self.__file_path, 'r', enconding='UFT-8') as f:
                jdic = json.load(f)
                for key in jdic:
                    value = date[jdic[key]["__class__"]](**jdic[key])
                    self.__object[key] = value
                    pass
        except:
            pass
