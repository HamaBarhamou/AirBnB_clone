#!/usr/bin/python3
""" Module for unittest"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        b = BaseModel()
        self.assertEqual(type("string"), type(b.id))


if __name__ == '__main__':
    unittest.main()
