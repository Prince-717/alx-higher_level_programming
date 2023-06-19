#!/usr/bin/python3
"""Unittest for the Square class."""
from io import StringIO
from contextlib import redirect_stdout
import unittest
from models.base import Base
from models.square import Square


class SquareTest(unittest.TestCase):
    """Tests for the Square class."""
    def setUp(self):
        """Initializes __nb_objects."""
        Base._Base__nb_objects = 0

    def test_id_type(self):
        """Checks if the id is an integer type."""
        personal_class = Square(2)
        self.assertIs(type(personal_class.id), int)

    def test_id_increments(self):
        """Checks if the ids increment."""
        for index in range(1, 6):
            with self.subTest(index=index):
                personal_class = Square(3)
                self.assertEqual(personal_class.id, index)

    def test_sets_id(self):
        """Checks if the id can be set."""
        personal_class = Square(5, 0, 0, 13)
        self.assertEqual(personal_class.id, 13)

    def test_sets_id_increments(self):
        """Checks if the ids increment after setting an id."""
        for index in range(1, 10):
            with self.subTest(index=index):
                if index == 5:
                    personal_class = Square(7, 0, 0, 13)
                    self.assertEqual(personal_class.id, 13)
                else:
                    personal_class = Square(9)
                    if index < 5:
                        self.assertEqual(personal_class.id, index)
                    else:
                        self.assertEqual(personal_class.id, index - 1)

    def test_sets_negative_id(self):
        """Checks if the id can be set with a negative integer."""
        personal_class = Square(11, 0, 0, -7)
        self.assertEqual(personal_class.id, -7)

    def test_gets_width(self):
        """Checks getter for width."""
        personal_class = Square(71)
        self.assertEqual(personal_class.width, 71)

    def test_gets_height(self):
        """Checks getter for height."""
        personal_class = Square(12)
        self.assertEqual(personal_class.height, 12)

    def test_gets_size(self):
        """Checks getter for size."""
        personal_class = Square(31)
        self.assertEqual(personal_class.size, 31)

    def test_gets_x(self):
        """Checks getter for x."""
        personal_class = Square(71, 12)
        self.assertEqual(personal_class.x, 12)

    def test_gets_y(self):
        """Checks getter for y."""
        personal_class = Square(71, 12, 21)
        self.assertEqual(personal_class.y, 21)

    def test_no_args(self):
        """Checks for missing arguments exception."""
        self.assertRaisesRegex(
            TypeError,
            "missing 1 required positional argument: 'size'",
            Square
        )

    def test_default_position_x(self):
        """Checks for default position attributes."""
        personal_class = Square(17)
        self.assertEqual(personal_class.x, 0)
        self.assertEqual(personal_class.y, 0)

    def test_default_position_y(self):
        """Checks for default position attributes."""
        personal_class = Square(17, 972)
        self.assertEqual(personal_class.y, 0)

    def test_width_type(self):
        """Checks width type."""
        self.assertRaisesRegex(
            TypeError,
            "width must be an integer",
            Square,
            [17]
        )
        self.assertRaisesRegex(
            TypeError,
            "width must be an integer",
            Square,
            "17"
        )
        self.assertRaisesRegex(
            TypeError,
            "width must be an integer",
            Square,
            (17,)
        )
        self.assertRaisesRegex(
            TypeError,
            "width must be an integer",
            Square,
            {"width": 17}
        )

    def test_width_value(self):
        """Checks width value."""
        self.assertRaisesRegex(
            ValueError,
            "width must be > 0",
            Square,
            0
        )
        self.assertRaisesRegex(
            ValueError,
            "width must be > 0",
            Square,
            -17
        )

    def test_x_type(self):
        """Checks x type."""
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Square,
            17, [12]
        )
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Square,
            17, "12"
        )
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Square,
            17, (12,)
        )
        self.assertRaisesRegex(
            TypeError,
            "x must be an integer",
            Square,
            17, {"x": 12}
        )

    def test_y_type(self):
        """Checks y type."""
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Square,
            17, 12, [16]
        )
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Square,
            17, 12, "16"
        )
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Square,
            17, 12, (16,)
        )
        self.assertRaisesRegex(
            TypeError,
            "y must be an integer",
            Square,
            17, 12, {"y": 16}
        )

    def test_x_value(self):
        """Checks x value."""
        self.assertRaisesRegex(
            ValueError,
            "x must be >= 0",
            Square,
            17, -12
        )

    def test_y_value(self):
        """Checks y value."""
        self.assertRaisesRegex(
            ValueError,
            "y must be >= 0",
            Square,
            17, 12, -16
        )

    def test_area(self):
        """Checks area."""
        personal_class = Square(6, 2, 16, 1)
        self.assertEqual(personal_class.area(), 36)

    def test_display(self):
        """Checks display."""
        personal_class = Square(3)
        outcome = "###\n###\n###\n"
        g = StringIO()
        with redirect_stdout(g):
            personal_class.display()
        result = g.getvalue()
        self.assertEqual(result, outcome)

    def test_str(self):
        """Checks string representation."""
        personal_class = Square(3, 1, 2, 6)
        self.assertEqual(personal_class.__str__(), "[Square] (6) 1/2 - 3")

    def test_display_position(self):
        """Checks display with a non-zero coordinates."""
        personal_class = Square(2, 2, 2)
        outcome = "\n\n  ##\n  ##\n"
        g = StringIO()
        with redirect_stdout(g):
            personal_class.display()
        result = g.getvalue()
        self.assertEqual(result, outcome)

    def test_update_args(self):
        """Checks update with args."""
        personal_class = Square(2, 1, 1, 6)
        personal_class.update(12)
        self.assertEqual(personal_class.id, 12)
        personal_class.update(12, 12)
        self.assertEqual(personal_class.width, 12)
        self.assertEqual(personal_class.height, 12)
        self.assertEqual(personal_class.size, 12)
        personal_class.update(12, 12, 11)
        self.assertEqual(personal_class.x, 11)
        personal_class.update(12, 12, 11, 11)
        self.assertEqual(personal_class.y, 11)


    def test_update_kwargs(self):
        """Checks update with kwargs."""
        personal_class = Square(10, 10, 10, 10)
        personal_class.update(size=1)
        self.assertEqual(personal_class.size, 1)

        personal_class.update(size=3, x=2)
        self.assertEqual(personal_class.width, 3)
        self.assertEqual(personal_class.x, 2)

        personal_class.update(y=1, size=2, x=3, id=89)
        self.assertEqual(personal_class.y, 1)
        self.assertEqual(personal_class.width, 2)
        self.assertEqual(personal_class.x, 3)
        self.assertEqual(personal_class.id, 89)

        personal_class.update(x=1, size=2, y=3)
        self.assertEqual(personal_class.x, 1)
        self.assertEqual(personal_class.height, 2)
        self.assertEqual(personal_class.y, 3)
        self.assertEqual(personal_class.width, 2)

    def test_dictionary(self):
        """Checks dictionary representation."""
        personal_class = Square(10, 1, 9)
        outcome = {'x': 1, 'size': 10, 'y': 9, 'id': 1}
        self.assertEqual(personal_class.to_dictionary(), outcome)
