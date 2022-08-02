#!/usr/bin/python3
"""Base class for the AirBnB clone"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Defines all attributes and method for other classes
    """

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """Initializes objects"""
        if kwargs:
            for key, value in kwargs.items()
            if key != '__class__':
                setattr(self, key, value)
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime-strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                storage.new(self)
=======
        """Initialization of BaseModel"""
        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at, %Y-%m-%dT%H:%M:%S.%f)
            self.updated_at = datetime.strptime(self.updated_at, %Y-%m-%dT%H:%M:%S.%f)
            
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
>>>>>>> 27681fe8a04bf08bc51d6364e06b6dc9ff994df0

                def __str__(self):
                    """Print name, id, dict"""
                    return '[{}] ({}) {}'.format(self.__class__.name, self.id, self.__dict__)

                def save(self):
                    """Updates the updated_at attribute with the current datetime"""
                    self.updated_at = datetime.now()
                    storage.save()

                    def to_dict(self):
                        """Returns dictionary"""
                        new_dict = self.__dict__.copy()
                        new_dict['__class__'] = self.__class__.name__
                        new_dict['created_at'] = self.created_at.isoformat()
                        new_dict['updated_at'] = self.updated_at.isoformat()

                        return new_dict
