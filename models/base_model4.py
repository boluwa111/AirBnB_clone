import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            exclude_attrs = ["__class__"]
            for attr, value in kwargs.items():
                if attr not in exclude_attrs:
                    if attr in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, attr, value)
            if not hasattr(self, "id"):
                self.id = str(uuid.uuid4())
            if not hasattr(self, "created_at"):
                self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
