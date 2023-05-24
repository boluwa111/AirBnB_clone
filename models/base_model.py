#! /bin/usr/python3

from uuid import uuid4

#! /usr/bin/python

import uuid

from datetime import datetime


class BaseModel:

    """Base model class."""

    id: str
    created_at: datetime
    updated_at: datetime

    def __init__(self):
        self.my_number = str(uuid4())

    """Base class for all other models."""

    id: str = None
    created_at: datetime = None
    updated_at: datetime = None

    def __init__(self):
        """Initialize a new BaseModel instance."""
        self.id = str(uuid.uuid4())

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.my_number, self.__dict__
        )

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of the object."""
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = dict_["created_at"].isoformat(
            )

        """Return a string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = dict_["created_at"].isoformat()

        dict_["updated_at"] = dict_["updated_at"].isoformat()
        return dict_
