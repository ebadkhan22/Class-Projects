class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "says woof!")

d = Dog("Buddy", "Labrador")
d.bark()
