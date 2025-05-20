class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

prod = Product(100)
print(prod.price)

prod.price = 150
print(prod.price)

del prod.price
# print(prod.price)  # This would raise an AttributeError now
