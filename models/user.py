#!/usr/bin/python3

from models.base_model import BaseModel

''' User class that inherits from BaseModel ''' 

class User(BaseModel):

    ''' Blue print for User object '''
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
