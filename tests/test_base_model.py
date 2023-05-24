#!/usr/bin/python3

import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.updated_at, model.created_at)

    def test_to_dict(self):
        model = BaseModel()
        dict_ = model.to_dict()
        self.assertIn("__class__", dict_)
        self.assertIn("id", dict_)
        self.assertIn("created_at", dict_)
        self.assertIn("updated_at", dict_)


if __name__ == "__main__":
    unittest.main()
