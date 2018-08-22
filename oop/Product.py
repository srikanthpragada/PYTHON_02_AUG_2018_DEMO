class Product:
    tax = 12  # static or class attribute

    # Constructor
    def __init__(self, name, price, qoh=0):
        self.__name = name
        self.__price = price
        self.__qoh = qoh

    # Methods
    def print_details(self):
        print(self.__name)
        print(self.__price)
        print(self.__qoh)

    def purchase(self, qty, price=-1):
        self.__qoh += qty
        if price >= 0:
            self.__price = price

    def sell(self, qty):
        self.__qoh -= qty

    def netprice(self):
        return self.__price + (self.__price * self.tax / 100)

    @staticmethod  # decorator
    def get_netprice(price):
        return price + (price * Product.tax / 100)

    def __str__(self):
        return "%s - %d" % (self.__name, self.__price)

    def __eq__(self, other):
        return self.__name == other.__name

    def __gt__(self, other):
        return self.__price > other.__price

    def __int__(self):
        return self.__price




Product.tax = 15

p1 = Product("iPad Air 2", 45000)  # Object
p2 = Product("iPhone X", 85000, 10)  # Object
p3 = Product("iPad Air 2", 45000)  # Object

print(id(p1), id(p2), id(p3))
print(p1 == p2, p1 != p3)
print(p2 > p3)

print(p1, str(p1), p1.__str__())
