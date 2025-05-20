class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

e = Employee("Alice")
d = Department(e)

print("Employee in department:", d.employee.name)
