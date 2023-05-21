#! /usr/bin/python

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base model class."""

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the object."""
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = dict_["created_at"].isoformat()
        dict_["updated_at"] = dict_["updated_at"].isoformat()
        return dict_
