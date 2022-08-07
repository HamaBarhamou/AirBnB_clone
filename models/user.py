#!/usr/bin/python3
"""class User than inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for the creation of new Users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
