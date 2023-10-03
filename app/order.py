from app.dish import Dish


class Order:
    def __init__(self,
                 dishes: list[Dish],
                 table_number):
        self.dishes = dishes
        self.table_number = table_number

    @property
    def dishes(self):
        return self._dishes

    @dishes.setter
    def dishes(self, dishes: list[Dish]):
        if (not isinstance(dishes, list)
                or not all(isinstance(dish, Dish) for dish in dishes)):
            raise TypeError("dishes must be a list['Dish']. "
                            f"Received {type(dishes)}: {dishes}")
        self._dishes = dishes

    @property
    def price(self):
        return self._calculate_price()

    def _calculate_price(self):
        return sum(dish.price for dish in self.dishes)

    def add_dish(self, dish: Dish):
        if not isinstance(dish, Dish):
            raise TypeError("dish must be a 'Dish' object. "
                            f"Received {type(dish)}: {dish}")
        self.dishes.append(dish)

    def remove_dish(self, dish: Dish):
        if not isinstance(dish, Dish):
            raise TypeError("dish must be a 'Dish' object. "
                            f"Received {type(dish)}: {dish}")
        self.dishes.remove(dish)

    def __repr__(self):
        dishes = ", ".join(repr(dish) for dish in self.dishes)
        return (f"Order(table_number={self.table_number}, "
                f"dishes=[{dishes}])")

    def __str__(self):
        dishes = "\t\n- ".join(str(dish) for dish in self.dishes)
        return (f"Order for table {self.table_number}:\n"
                f"- {dishes}\n"
                f"Total price: {self.price}")
