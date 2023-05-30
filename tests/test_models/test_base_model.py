#! /bin/usr/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_instance_attributes(self):
        my_model = BaseModel()
        self.assertIsNone(my_model.name)
        self.assertIsNone(my_model.my_number)
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_str_representation(self):
        my_model = BaseModel()
        expected_output = f"[BaseModel] ({my_model.id}) {my_model.to_dict()}"
        self.assertEqual(str(my_model), expected_output)

    def test_save_method(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel(name="My_First_Model", my_number=89)
        dict_representation = my_model.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(dict_representation["name"], "My_First_Model")
        self.assertEqual(dict_representation["my_number"], 89)

if __name__ == '__main__':
    unittest.main()
