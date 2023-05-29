
import unittest
import uuid
from datetime import datetime


class BaseModelTest(unittest.TestCase):

    def test_init(self):
        """Test the `__init__` method."""
        model = BaseModel()
        self.assertEqual(model.id, str(uuid.uuid4()))
        self.assertEqual(model.created_at, datetime.now())
        self.assertEqual(model.updated_at, datetime.now())

    def test_str(self):
        """Test the `__str__` method."""
        model = BaseModel()
        self.assertEqual(str(model), "[BaseModel] ({}) {}".format(model.__class__.__name__, model.id, model.__dict__))

    def test_save(self):
        """Test the `save` method."""
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.updated_at, datetime.now())

    def test_to_dict(self):
        """Test the `to_dict` method."""
        model = BaseModel()
        dic = model.to_dict()
        self.assertEqual(dic["__class__"], model.__class__.__name__)
        self.assertEqual(dic["created_at"], model.created_at.isoformat())
        self.assertEqual(dic["updated_at"], model.updated_at.isoformat())
