#!/usr/bin/python3
"""Module for BaseModel class"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel"""
        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at,  %Y-%m-%dT%H:%M:%S.%f)
            self.updated_at = datetime.strptime(self.updated_at,  %Y-%m-%dT%H:%M:%S.%f)
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

            def __str__(self):
                """Return a string representation of an object"""
                return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

            def save(self):
                """Updates the date for updated_at"""
                self.updated_at = datetime.now()
                storage.save()

                def to_dict(self):
                    """Returns dictionary containing
                    all keys/values of __dict__
                    """
                    newdict = self.__dict__.copy()
                    newdict['__class__'] = self.__class__.__name__
                    newdict['created_at'] = self.created_at.isoformat()
                    newdict['updated_at'] = self.updated_at.isoformat()

                    return newdict
