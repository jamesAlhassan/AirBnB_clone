#!/usr/bin/python3
'''base_model script'''

from uuid import uuid4 as ui
from datetime import datetime as dt
from models import storage


class BaseModel:
    """
    Initializes an instance of the BaseModel class.

    If keyword arguments are passed, they are used to set the corresponding
    attributes. If not, a unique identifier is generated and the created_at
    and updated_at attributes are set to the current date and time.
    """
    def __init__(self, *args, **kwargs):
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = dt.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = dt.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(ui())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        '''Returns a string representation of the class'''

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''Updates the public instance with the current date and time'''

        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        '''
        Returns a dictionary representation of the class instance
        Returns a dict with the keys, values of __dict__'''

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
