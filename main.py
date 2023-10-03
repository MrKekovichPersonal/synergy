from app.dish import Dish
from app.order import Order
from app.utils.decorators import deprecated


@deprecated(reason="Use normal print instead")
def print_order(order):
    print(order)


if __name__ == '__main__':
    # Зачем могут существовать пустые заказы? Вот и я так подумал и решил отрезать такой функционал
    dish1 = Dish("Стейк", 25.99)
    dish2 = Dish("Салат", 12.99)
    dish3 = Dish("Паста", 18.99)

    # Создание заказов
    order1 = Order([dish1, dish3], "Столик 1", )
    order2 = Order([dish2], "Столик 2", )

    # Добавление блюд в заказы
    order1.add_dish(dish1)
    order1.add_dish(dish3)
    order2.add_dish(dish2)

    # Вывод информации о заказах
    print_order(order1)
