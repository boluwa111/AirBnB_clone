#! /bin/usr/python3

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class for all other models."""

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self, *args, **kwargs):
        self.name = None
        self.my_number = None
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    self.name = kwargs["name"]
                    self.my_number = kwargs["my_number"]
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """Updates the public instance attribute `updated_at` with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        dic = {}
        dict_ = self.__dict__.copy()

        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = dict_["created_at"].isoformat()

        dict_["updated_at"] = dict_["updated_at"].isoformat()
        keys = ["id","created_at","my_number","updated_at","name"]
        for i in keys:
            dic[i] = dict_[i]
        return dic
