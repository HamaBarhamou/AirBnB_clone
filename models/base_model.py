#!/usr/bin/python3
"""class BaseModel"""
import uuid
from datetime import datetime
<<<<<<< HEAD
import models

"""from models import storage"""




class BaseModel:
    """
    Defines all common attributes and methods
    for other classes
    """
    def __init__(self, *args, *kwargs):
        """Constructor of a BaseModel"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                            value, "%d/%m/%Y %H:%M:%S")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                            value, "%d/%m/%Y %H:%M:%S")
                elif key != "__class__":
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    models.storage.new(self)

    def __str__(self):
        """Return string representation for an object"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """Returns dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
