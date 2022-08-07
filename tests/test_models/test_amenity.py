#!/usr/bin/python3
"""Unittest"""
import unittest
from models.amenity import Amenity
import datetime


class TestAmenity(unittest.TestCase):
    """Testing attributes of amenity class"""

    amen = Amenity()

    def test_class(self):
        """¿Class exists?"""
        resource = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.ame)), resource)

    def test_user1(self):
        """Amenity is a subclass of BaseModel?"""
        self.assertIsInstance(self.ame, Amenity)

    def test_attributes(self):
        """Attributes check"""
        self.assertTrue(hasattr(self.ame, 'name'))
        self.assertTrue(hasattr(self.ame, 'id'))
        self.assertTrue(hasattr(self.ame, 'created_at'))
        self.assertTrue(hasattr(self.ame, 'updated_at'))

    def test_type_attribute(self):
        """Checks for the correct type of attributes"""
        self.assertIsInstance(self.ame.name, str)
        self.assertIsInstance(self.ame.id, str)
        self.assertIsInstance(self.ame.created_at, datetime.datetime)
        serlf.assertIsInstance(self.ame.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
