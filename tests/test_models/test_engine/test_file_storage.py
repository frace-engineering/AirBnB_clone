#!/usr/bin/python3
"""Test module for Storage class"""

import unittest
from models.engine.file_storage import FileStorage
from models import storage
from tests.reset_storage import resetStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Sets up the test suite"""

        pass

    def tearDown(self):
        """Tears down the test suite"""
        resetStorage()
        pass

    # Case 0: test class instantiation
    def test_5_instantiation(self):
        """Tests the instantiation of the class"""

        self.assertEqual(type(storage).__name__, "FileStorage")
    
    # Case 1: init with no args
    def test_5_init_no_args(self):
        """Tests instantiation with no args"""

        resetStorage()
        with self.assertRaises(TypeError) as e:
            FileStorage.__init__()
        exception = str(e.exception)
        msg = "descriptor '__init__' of 'object' object needs an argument"
        self.assertEqual(exception, msg)
    
    # Case 2: init with too much args
    def test_5_init_too_much_args(self):
        """Init with too much args"""

        resetStorage()
        with self.assertRaises(TypeError) as e:
            storage = FileStorage("alx", "holberton", 98, 4, 128)
        exception = str(e.exception)
        msg = "FileStorage() takes no arguments"
        self.assertEqual(exception, msg)
    
    # Case 3: test the class attributes
    def test_5_attributes(self):
        """Tests the attributes of FileStorage class"""

        resetStorage()
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertTrue(getattr(FileStorage, "_FileStorage__objects"), {})

        