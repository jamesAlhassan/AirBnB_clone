#!/usr/bin/python3
"""Base Model Module"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    BaseModel class which all other classes inherit from.
    This class provides a basic implementation of id, created_at, and updated_at attributes, 
    as well as methods for saving, updating and returning a dictionary representation of an instance.
    """

    def __init__(self, *args, **kwargs):
        """Initialize an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute to the current time and save the instance to storage"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        dict_representation = self.__dict__.copy()
        dict_representation["__class__"] = self.__class__.__name__
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        return dict_representation
