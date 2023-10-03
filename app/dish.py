class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Dish(name={self.name}, price={self.price})"

    def __str__(self):
        return f"name: {self.name} | price: {self.price}"
