#!/usr/bin/python3
"""FileStorage module
Serializes instances to JSON file
and deserializes JSON file to instances
"""

import json
import os
import datetime


class FileStorage:
    """Serializes instances to JSON file and deserializes
    instances from JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects

        Returns: FileStorage.__objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objets the obj with key <obj class name>.id

        Args:
            -obj: the object to store in the __objects

        Returns: None
        """

        key = "{}.{}".format(type(obj).__name__, str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path:__file_path)

        Returns: None
        """

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references

        Returns: A dictionary of valid classes and their refrences
        """

        from models.base_model import BaseModel

        classes = {"BaseModel": BaseModel}

        return classes

    def reload(self):
        """Deserializes the JSON file to __objects

        Return: None
        """

        if not os.path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            my_obj = json.load(f)
            my_obj = {k: self.classes()[v["__class__"]](**v)
                      for k, v in my_obj.items()}

            FileStorage.__objects = my_obj

    def attributes(self):
        """Returns the valid attributes and their types
        for the various classes

        Returns: The various classes and their attributes
        """

        attributes = {
            "BaseModel":
            {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            }
        }

        return attributes
