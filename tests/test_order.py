from unittest import TestCase

from app.dish import Dish
from app.order import Order


class TestOrder(TestCase):
    def test_create_valid(self):
        dish = Dish("test", 10)
        order = Order([dish], 1)
        self.assertEqual(order.dishes, [dish])
        self.assertEqual(order.table_number, 1)

    def test_create_invalid(self):
        dish = Dish("test", 10)
        with self.assertRaises(TypeError):
            Order(1, 1)
        with self.assertRaises(TypeError):
            Order(dish, 1)
        with self.assertRaises(TypeError):
            Order([1], 1)

    def test_add_dish(self):
        dish = Dish("test", 10)
        order = Order([dish], 1)
        order.add_dish(dish)
        self.assertEqual(order.dishes, [dish, dish])

    def test_remove_dish(self):
        dish = Dish("test", 10)
        order = Order([dish], 1)
        order.remove_dish(dish)
        self.assertEqual(order.dishes, [])

    def test_price(self):
        dish = Dish("test", 10)
        order = Order([dish, dish], 1)
        self.assertEqual(order.price, 20)
