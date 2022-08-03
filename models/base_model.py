#!/usr/bin/python3
"""class BaseModel"""
import uuid
from uuid import uuid4
from datetime import datetime

from models import storage


class BaseModel:
    """
    Defines all common attributes and methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Constructor of a BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        #models.storage.new(self)
        storage.new(self)
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    date = value[0:10] + " " + value[11:]
                    self.created_at = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
                elif key == "updated_at":
                    #print("val:",value)
                    date = value[0:10] + " " + value[11:]
                    #print("val:",date)
                    self.updated_at = datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
                elif key != "__class__":
                    setattr(self, key, value)
                    
        
    def __str__(self):
        """Return string representation for an object"""
        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        #models.storage.save()
        storage.save()


    def to_dict(self):
        """Returns dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
