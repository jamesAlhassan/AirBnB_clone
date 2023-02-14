#!/usr/bin/python

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class handles the storage and retrieval of objects in a JSON fil
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects in __objects"""
        return FileStorage.__objects

    def new(self, obj):
        key = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Adds an object to the __objects dictionary"""

        with open(FileStorage.__file_path, 'w') as f:

            ''' Serializes the __objects dictionary to the JSON file '''
            sdict = {}
            for key, item in FileStorage.__objects.items():
                sdict[key] = item.to_dict()
            json.dump(sdict, f)

    def reload(self):
        ''' Deserializes the JSON file to the __objects dictionary'''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                sdict = json.load(f)
                for key, item in sdict.items():
                    class_name = item.get("__class__", None)
                    if class_name is not None:
                        if class_name == "BaseModel":
                            FileStorage.__objects[key] = BaseModel(**item)
                        elif class_name == "User":
                            FileStorage.__objects[key] = User(**item)
                        elif class_name == "Place":
                            FileStorage.__objects[key] = Place(**item)
                        elif class_name == "State":
                            FileStorage.__objects[key] = State(**item)
                        elif class_name == "City":
                            FileStorage.__objects[key] = City(**item)
                        elif class_name == "Amenity":
                            FileStorage.__objects[key] = Amenity(**item)
                        elif class_name == "Review":
                            FileStorage.__objects[key] = Review(**item)
        except FileNotFoundError:
            pass
