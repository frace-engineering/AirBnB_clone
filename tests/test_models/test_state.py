#!/usr/bin/python3
"""Unittest for the State class"""

import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage
from tests.reset_storage import resetStorage


class TestState(unittest.TestCase):
    """Test suite for the State class"""

    def setUp(self):
        """Sets up the test suite"""

        resetStorage()
        pass

    def tearDown(self):
        """Tears down the test suite"""

        resetStorage()
        pass

    # Case 0: Instantiate State
    def test_9_instantiation(self):
        """Tests instantiation of class State"""

        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(issubclass(type(state), BaseModel))

    # Case 1: Attributes
    def test_9_attributes(self):
        """Test the attributes of state"""

        attributes = storage.attributes()["State"]
        state = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(state, k))
            self.assertEqual(type(getattr(state, k, None)), v)


if __name__ == "__main__":
    unittest.main()
