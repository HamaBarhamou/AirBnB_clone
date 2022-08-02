#!/usr/bin/python3
"""Base class for all models in AirBnB clone"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes and methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes objetcs using dictionary"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = datetime.now()
                    storage.new(self)

                    def __str__(self):
                        """Print clas name, self id, dictionary"""
                        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

                    def save(self):
                        """Updates the updated_at date time"""
                        self.updated_at = datetime.now()
                        storage.save()

                        def to_dict(self):
                            """Returns dictionary"""
                            new_dict = self.__dict__.copy()
                            new_dict['__class__'] = self.__class__.name__
                            new_dict['updated_at'] = self.updated_at.isoformat()
                            new_dict['created_at'] = self.created_at.isoformat()
                            return new_dict
