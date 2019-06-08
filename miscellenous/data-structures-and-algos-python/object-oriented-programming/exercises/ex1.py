# Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.


class Flower:
    def __init__(self, name, petals, price):
        if not isinstance(name, str) or not isinstance(petals, int) or not (isinstance(price, float) and isinstance(price, int)):
            raise TypeError(
                "Incorrect types entered, the name should be a string, petals should be an integer and price should be a float")
        self._name = name
        self._petals = petals
        self._price = float(price)

    def __repr__(self):
        return f'name: {self._name}, petals: {self._petals}, price: {self._price}'

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Must be a string")
        self._name = name

    def set_petals(self, petals):
        if not isinstance(petals, int):
            raise TypeError("Must be an integer")
        self._petals = petals

    def set_price(self, price):
        if not isinstance(price, float) and not isinstance(price, int):
            raise TypeError('Must be a number')
        self._price = float(price)

    def get_name(self):
        return self._name

    def get_petals(self):
        return self._petals

    def get_price(self):
        return self._price


my_flower = Flower("Satosa", 5, 20)
# my_flower2 = Flower('Kinf', 'd', 3)
print(my_flower)
print(my_flower.get_name())
print(my_flower.set_price(58))
print(my_flower)
# print(my_flower2)


print(isinstance(1, float))
