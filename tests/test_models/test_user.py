#!/usr/bin/python3
"""Test for the User class that inherits from BaseModel"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Test case for user"""
    def test_attributes(self):
        """test a class attribute"""
        u = User()
        self.assertTrue(hasattr(User, "first_name")
                and hasattr(User, "last_name"))

    def test_names(self):
        """Firstname, lastname attributes"""
        u = User()
        self.assertIs(type(u.first_name), str)
        self.asserIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

    def test_user_subclass(self):
        """Checks if User is a subclass of BaseModel"""
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
