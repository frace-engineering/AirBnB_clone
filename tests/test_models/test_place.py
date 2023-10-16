#!/usr/bin/python3
"""Module for Place class tests"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
from tests.reset_storage import resetStorage


class TestPlace(unittest.TestCase):
    """Test suite for Place class"""

    def setup(self):
        """Sets up the TestPlace test suite"""

        resetStorage()
        pass

    def tearDown(self):
        """Tears down the TestPlace module"""

        resetStorage()
        pass

    # Case 0: Instantiation
    def test_9_instantiate_place(self):
        """Tests instantiation of Place class"""

        place = Place()
        self.assertIsInstance(place, Place)
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(type(place), BaseModel))

    # Case 1: attributes
    def test_9_attributes_place(self):
        """Test attributes of Place class"""

        place = Place()
        attributes = storage.attributes()["Place"]
        for k, v in attributes.items():
            self.assertTrue(hasattr(place, k))
            self.assertEqual(type(getattr(place, k, None)), v)


if __name__ == "__main__":
    unittest.main()
