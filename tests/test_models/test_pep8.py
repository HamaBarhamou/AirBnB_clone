#!/usr/bin/python3
""" Module for unittest"""

import unittest
import pycodestyle


class TestBaseModel(unittest.TestCase):
    def test_pep8_console(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_basemodel(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['test_base_model.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_basemodeldic(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['test_base_model_dict.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_savereloadbasemodel(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['test_save_reload_base_model.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_modelsbasemodel(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_models__init__(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/__init__.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_modelsengin__init__(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/__init__.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_modelsenginfilestorage(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_testmodules__init__(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/__init__.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_testmodulestestebasemodule(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(
            result.total_errors, 0,
            "Found code style errors (and warnings).")

    def test_pep8_testmoduletestpep8(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_pep8.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_savereloaduser(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['test_save_reload_user.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_amenity(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_city(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_place(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_review(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/review.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_state(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/state.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_user(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
