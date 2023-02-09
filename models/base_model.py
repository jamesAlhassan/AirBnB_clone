# !/usr/bin/python

from uuid import uuid4 as ui
from datetime import datetime as dt

class BaseModel:
    def __init__(self):
        self.id = str(ui())
        self.created_at = dt.now()
        self.updated_at = dt.now()

    def __str__(self):
        return f'[{type(self).__name__}, {self.id}, {self.__dict__}]'

    def save(self):
        self.updated_at = dt.now()

    def to_dict(self):
        my_dict = self.__dict__
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
