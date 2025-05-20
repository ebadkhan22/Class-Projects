class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

t = Teacher("Ebad", "Mathematics")
t.show()
