#!/usr/bin/python3
"""Unittest module for the User class"""

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from tests.reset_storage import resetStorage


class TestUser(unittest.TestCase):
    """Test suite for the User class"""

    def setUp(self):
        """sets up the test suite"""

        pass

    def tearDown(self):
        """tears down the test suite"""

        resetStorage()
        pass

    # Case 1: instantiation
    def test_8_instantiation(self):
        """Test creation of new instance of User"""

        user = User()
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")

    # Case 2: test for user attributes
    def test_8_attribs(self):
        """Tests the attributes of the user instance"""

        attributes = storage.attributes()["User"]
        user = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(user, k))
            self.assertEqual(type(getattr(user, k, None)), v)


if __name__ == "__main__":
    unittest.main()
