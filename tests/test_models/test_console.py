#!/usr/bin/python3

import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id_is_unique(self):
        # Create two instances of the BaseModel class.
        model1 = BaseModel()
        model2 = BaseModel()

        # Assert that the IDs of the two instances are different.
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_is_set_correctly(self):
        # Create an instance of the BaseModel class.
        model = BaseModel()

        # Assert that the created_at attribute is set to the current date and time.
        self.assertEqual(model.created_at, datetime.now())

    def test_updated_at_is_set_correctly(self):
        # Create an instance of the BaseModel class.
        model = BaseModel()

        # Update the model.
        model.name = "John Doe"

        # Assert that the updated_at attribute is set to the current date and time.
        self.assertEqual(model.updated_at, datetime.now())

    def test_to_dict_returns_a_dictionary_representation_of_the_object(self):
        # Create an instance of the BaseModel class.
        model = BaseModel()

        # Assert that the to_dict() method returns a dictionary representation of the object.
        self.assertDictEqual(model.to_dict(), {
            "id": model.id,
            "created_at": model.created_at.isoformat(),
            "updated_at": model.updated_at.isoformat(),
        })


if __name__ == "__main__":
    unittest.main()
