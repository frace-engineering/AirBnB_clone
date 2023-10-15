#!/usr/bin/python3
"""Module for TESTHBNBCommand class"""

import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import os


class TestHBNBCommand(unittest.TestCase):
    """Tests HBNBCommand console"""

    def setUp(self):
        """Sets the test up"""

        if os.path.isfile("file.json"):
            os.remove("file.json")
        