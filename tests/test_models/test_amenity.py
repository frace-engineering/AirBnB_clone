#!/usr/bin/python3
"""Test module for the Amenity class"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from tests.reset_storage import resetStorage


class TestAmenity(unittest.TestCase):
    """The test suite class for Amenity class"""

    def setup(self):
        """Sets up the test suite"""

        resetStorage()
        pass

    def tearDown(self):
        """Tears downt he test suite"""

        resetStorage()
        pass

    # Case 0: Instantiate Amenity class
    def test_9_instantiate_amenity(self):
        """Test for Amenity instances"""

        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        msg = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(amenity)), msg)
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(type(amenity), BaseModel))

    # Case 1: attributes
    def test_9_attributes_amenity(self):
        """Test the attributes of Amenity instance"""

        amenity = Amenity()
        attributes = storage.attributes()["Amenity"]
        for k, v in attributes.items():
            self.assertTrue(hasattr(amenity, k))
            self.assertEqual(type(getattr(amenity, k)), v)


if __name__ == "__main__":
    unittest.main()
