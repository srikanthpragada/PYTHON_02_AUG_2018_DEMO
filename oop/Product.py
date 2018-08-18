class Product:
    # Constructor
    def __init__(self, name, price, qoh=0):
        self.name = name
        self.price = price
        self.qoh = qoh

    # Methods
    def print_details(self):
        print(self.name)
        print(self.price)
        print(self.qoh)

    def purchase(self, qty, price=-1):
        self.qoh += qty
        if price >= 0:
            self.price = price

    def sell(self, qty):
        self.qoh -= qty


p1 = Product("iPad Air 2", 45000)  # Object
p1.price = 40000
p1.purchase(5)
# p1.purchase(5, 42000)
p1.print_details()

p2 = Product("iPhone X", 85000, 10)  # Object
p2.print_details()
