#!/usr/bin/python3
"""Base model clas that defines all common
attributes/methods for other classes"""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """The base model for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the class and/or instance

        Returns: None
        """

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime

        Returns: None
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values
        of  __dict__ of the instance

        Returns: None
        """

        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = type(self).__name__
        inst_dict["created_at"] = inst_dict["created_at"].isoformat()
        inst_dict["updated_at"] = inst_dict["updated_at"].isoformat()
        return inst_dict

    def __str__(self):
        """Prints a human readable version of the instance

        Returns: None
        """

        string = "[{}] ({}) {}".format(type(self).__name__,
                                       self.id, self.__dict__)

        return string
