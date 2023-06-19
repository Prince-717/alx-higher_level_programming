#!/usr/bin/python3
"""Unittest for the Base class."""
import unittest
import json
from models.base import Base


class BaseTest(unittest.TestCase):
    """Tests for the Base class."""
    def setUp(self):
        """Initializes the __nb_objects attribute before each test."""
        self.assertIs(hasattr(Base, "_Base__nb_objects"), True)
        Base._Base__nb_objects = 0

    def test_id_type(self):
        """Checks if the id is an integer type."""
        personal_class = Base()
        self.assertIs(type(personal_class.id), int)

    def test_id_increments(self):
        """Checks if the ids increment."""
        for index in range(1, 6):
            with self.subTest(index=index):
                personal_class = Base()
                self.assertEqual(personal_class.id, index)

    def test_sets_id(self):
        """Checks if the id can be set."""
        personal_class = Base(13)
        self.assertEqual(personal_class.id, 13)

    def test_sets_id_increments(self):
        """Checks if the ids increment after setting an id."""
        for index in range(1, 10):
            with self.subTest(index=index):
                if index == 5:
                    personal_class = Base(13)
                    self.assertEqual(personal_class.id, 13)
                else:
                    personal_class = Base()
                    if index < 5:
                        self.assertEqual(personal_class.id, index)
                    else:
                        self.assertEqual(personal_class.id, index - 1)

    def test_sets_negative_id(self):
        """Checks if the id can be set with a negative integer."""
        personal_class = Base(-7)
        self.assertEqual(personal_class.id, -7)

    def test_to_json(self):
        """Checks the json represntation."""
        entry = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        outcome = json.dumps(entry)
        self.assertEqual(Base.to_json_string(entry), outcome)

    def test_to_json_empty(self):
        """Checks the json represntation with an empty list."""
        entry = []
        outcome = "[]"
        self.assertEqual(Base.to_json_string(entry), outcome)

    def test_to_json_none(self):
        """Checks the json represntation with None."""
        entry = None
        outcome = "[]"
        self.assertEqual(Base.to_json_string(entry), outcome)
