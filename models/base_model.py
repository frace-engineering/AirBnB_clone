#!/usr/bin/python3
"""Base model clas that defines all common
attributes/methods for other classes"""

from datetime import datetime
import uuid


class BaseModel:
    """The base model for other classes"""

    def __init__(self):
        """Initializes the class and/or instance

        Returns: None
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime

        Returns: None
        """

        self.updated_at = datetime.now()

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
