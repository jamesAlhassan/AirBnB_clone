#!/usr/bin/python3

from models.base_model import BaseModel

'''Review class that inherits from BaseModel'''

class Review(BaseModel):

    ''' Blue print for Review object '''
    
    place_id = ""
    user_id = ""
    text = ""
