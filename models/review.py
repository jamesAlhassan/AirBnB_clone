#!/usr/bin/python3
'''Review class that inherits from BaseModel'''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' Blue print for Review object '''

    place_id = ""
    user_id = ""
    text = ""
