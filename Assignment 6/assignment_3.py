class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "is starting...")

c = Car("Toyota")
print("Brand:", c.brand)
c.start()
