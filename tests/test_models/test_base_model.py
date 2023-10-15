#!/usr/bin/python3
"""Unittest for BaseModel class and instances"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import uuid
import time


class TestBaseModel(unittest.TestCase):
    """The test cases for the BaseModel class and its instances"""

    # Case 0: setup
    def setUp(self):
        """sets up the entire test suite"""

        pass

    # Case 1: teardown
    def tearDown(self):
        """tears down the entire test suite"""

        pass

    # Case 2: Instantiation
    def test_3_instantiation(self):
        """Tests instantiation of the BaseModel"""

        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(issubclass(type(model), BaseModel))
        msg = "<class 'models.base_model.BaseModel'>"
        self.assertEqual(str(type(model)), msg)

    # Case 3: unique ids are assgined for multiple intance creations
    def test_3_id(self):
        """Test unique ids assinged for multiple instance creations"""

        models = [BaseModel().id for i in range(100)]
        self.assertEqual(len(set(models)), len(models))

    # Case 4: No args
    def test_3_no_args(self):
        """Tests no arg to init method of BaseModel"""

        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        exception = str(e.exception)
        msg = "BaseModel.__init__() missing 1 "
        msg = msg + "required positional argument: 'self'"
        self.assertEqual(exception, msg)

    # Case 5: Too many args
    def test_3_too_much_args(self):
        """Test with too many args to init method of BaseModel"""

        with self.assertRaises(TypeError) as e:
            BaseModel.__init__("alx", 98)
        exception = str(e.exception)
        msg = "BaseModel.__init__() takes 1 "
        msg = msg + "positional argument but 2 were given"
        self.assertEqual(exception, msg)

    # Case 6: test created_at and updated_at
    def test_3_datetime(self):
        """Test the values of created_at and updated_at"""

        model = BaseModel()
        diff = model.created_at - model.updated_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = model.updated_at - model.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    # Case 7: test we instance can update itself
    def test_3_save(self):
        """Tests an instance can update itself by calling save method"""

        model = BaseModel()
        time.sleep(0.5)
        now = datetime.now()
        model.save()
        diff = model.updated_at - now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    # Case 8: test the __str__ method
    def test_3_str(self):
        """Test the __str__ method"""

        model = BaseModel()

    # Case 9: test the to_dict method
    def test_3_to_dict(self):
        """Tests the public instance method to_dict()"""

        model = BaseModel()
        model.name = "My first model"
        model.number = 89
        model_d = model.to_dict()
        self.assertEqual(model_d["id"], model.id)
        self.assertEqual(model_d["name"], model.name)
        self.assertEqual(model_d["number"], model.number)
        self.assertEqual(model_d["created_at"], model.created_at.isoformat())
        self.assertEqual(model_d["updated_at"], model.updated_at.isoformat())
        self.assertEqual(model_d["__class__"], type(model).__name__)

    # Case 10: test no argument to the dict method
    def test_3_dict_no_args(self):
        """Test to_dict() without an argument"""

        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict()
        exception = str(e.exception)
        msg = "BaseModel.to_dict() missing 1 required "
        msg = msg + "positional argument: 'self'"
        self.assertEqual(exception, msg)

    # Case 11: test too much args to dict method
    def test_3_dict_too_much_args(self):
        """Test too much args to dict"""

        with self.assertRaises(TypeError) as e:
            BaseModel.to_dict("alx", 98)
        exception = str(e.exception)
        msg = "BaseModel.to_dict() takes 1 "
        msg = msg + "positional argument but 2 were given"
        self.assertEqual(exception, msg)
