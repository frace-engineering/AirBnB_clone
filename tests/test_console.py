#!/usr/bin/python3
"""Module for TESTHBNBCommand class"""

import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os
from tests.reset_storage import resetStorage


class TestHBNBCommand(unittest.TestCase):
    """Tests HBNBCommand console"""

    def setUp(self):
        """Sets the test up"""

        if os.path.isfile("file.json"):
            os.remove("file.json")
            resetStorage()
    
    def tearDown(self):
        """Tears the test down"""

        resetStorage()
    
    def test_1(self):
        """testing"""

        pass