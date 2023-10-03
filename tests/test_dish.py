from unittest import TestCase

from app.dish import Dish


class TestDish(TestCase):
    def test_create(self):
        dish = Dish("test", 10)
        self.assertEqual(dish.name, "test")
        self.assertEqual(dish.price, 10)


