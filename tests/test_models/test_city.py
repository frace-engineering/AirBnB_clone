#!/usr/bin/python3
"""Module for the City class"""

import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from tests.reset_storage import resetStorage


class TestCity(unittest.TestCase):
    """The TestCity suite"""

    def setup(self):
        """Sets up the test suite"""

        resetStorage()
        pass

    def tearDown(self):
        """Tears the test suite"""

        resetStorage()
        pass

    # Case 0: instantiation
    def test_9_instiantiate_city(self):
        """Tests City class instantiation"""

        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(type(city), BaseModel))

    # Case 1: attributes
    def test_9_attributes_city(self):
        """Test City instance attributes"""

        attributes = storage.attributes()["City"]
        city = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(city, k))
            self.assertEqual(type(getattr(city, k, None)), v)


if __name__ == "__main__":
    unittest.main()
