import unittest
from uuid import UUID
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel(name="My_Model", my_number=42)
        self.assertIsInstance(model.id, UUID)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.name, "My_Model")
        self.assertEqual(model.my_number, 42)

    def test_save(self):
        model = BaseModel()
        created_at = model.created_at
        model.save()
        self.assertNotEqual(model.updated_at, created_at)

    def test_to_dict(self):
        model = BaseModel(name="My_Model", my_number=42)
        data = model.to_dict()
        self.assertIsInstance(data, dict)
        self.assertEqual(data["id"], str(model.id))
        self.assertEqual(data["created_at"], model.created_at.isoformat())
        self.assertEqual(data["updated_at"], model.updated_at.isoformat())
        self.assertEqual(data["name"], "My_Model")
        self.assertEqual(data["my_number"], 42)

if __name__ == '__main__':
    unittest.main()
