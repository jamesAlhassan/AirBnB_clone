#!/usr/bin/python3

import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = type(obj).__name__ +  + obj.id
        FileStorage.__objects[key] = obj

    def save(self)
        with open(FileStorage.__file_path, 'a') as f:
            sdict = {}
            for key, value in FileStorage.__objects.items():
                sdict[key] = item.to_dict()
            json.dump(sdict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                sdict = json.load(f)
                
                    else:
                        pass
        except FileNotFoundError:
            pass
