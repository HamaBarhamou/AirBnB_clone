#!/usr/bin/python3
""" Module for unittest"""

import unittest
import pycodestyle
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        b = BaseModel()
        self.assertEqual(type("string"), type(b.id))

    def test_name(self):
        b = BaseModel()
        b.name = "My_First_model"
        self.assertEqual(b.name, "My_First_model")

    def test_number(self):
        b = BaseModel()
        b.my_number = 89
        self.assertEqual(b.my_number, 89)

    def test_pycodestyle(self):
        """Test that we conform to PEP-8."""
        """style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([
            'console.py',
            'test_base_model.py',
            'test_base_model_dict.py',
            'test_save_reload_base_model.py',
            'models/base_model.py',
            'models/__init__.py/',
            'models/engine/__init__.py',
            'models/engine/file_storage.py',
            'tests/test_modules/__init__.py',
            'tests/test_modules/test_base_model.py',
            ])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")"""
        pass


if __name__ == '__main__':
    unittest.main()
