#! /bin/usr/python3

import uuid
from datetime import datetime


class BaseModel:


    """Base class for all other models."""

    id: str = None
    created_at: datetime = None
    updated_at: datetime = None

    def __init__(self):
        """Initialize a new BaseModel instance."""
        
        self.my_number = None
        self.name = None
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        

    def __str__(self):

        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update the updated_at attribute."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the object."""
        dic = {}
        dict_ = self.__dict__.copy()
        
        dict_["__class__"] = self.__class__.__name__
        dict_["created_at"] = dict_["created_at"].isoformat()

        dict_["updated_at"] = dict_["updated_at"].isoformat()
        keys = ["my_number","name","__class__","updated_at","id","created_at"]
        for i in keys:
            dic[i] = dict_[i]
        return dic
