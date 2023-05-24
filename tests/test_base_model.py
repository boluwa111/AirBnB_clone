#!/usr/bin/python3

import unittest
from datetime import datetime
from unittest.mock import patch
from my_module import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_initialization(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsNotNone(self.base_model.created_at)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsNotNone(self.base_model.updated_at)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    @patch('my_module.datetime')
    def test_save_updates_updated_at(self, mock_datetime):
        test_datetime = datetime(2023, 5, 21, 12, 0, 0)
        mock_datetime.now.return_value = test_datetime

        self.base_model.save()

        self.assertEqual(self.base_model.updated_at, test_datetime)

    def test_to_dict_returns_dict_representation(self):
        expected_dict = {
            '__class__': 'BaseModel',
            'id': self.base_model.id,
            'created_at': self.base_model.created_at.isoformat(),
            'updated_at': self.base_model.updated_at.isoformat()
        }

        result_dict = self.base_model.to_dict()

        self.assertEqual(result_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
