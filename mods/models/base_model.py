#!/usr/bin/python3
"""
parent class that will inherit
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the base model of the AIRBNB """

    def __init__(self, *args, **kwargs):
        """initialize a new basemodel
        Args:
            *args
            **kwargs
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v

    def __str__(self):
        """Returns classname id and dict attribute"""
        classname = self.__class__.__name__
        return "[{}] ({}) {} ".format(classname, self.id, self.__dict__)

    def save(self):
        """update updated_at to current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        r_dict = self.__dict__
        r_dict["create_at"] = self.created_at.isoformat()
        r_dict["updated_at"] = self.updated_at.isoformat()
        r_dict["__class__"] = self.__class__.__name__

        return r_dict
