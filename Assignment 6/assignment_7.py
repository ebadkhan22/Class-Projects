class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

e = Employee("Ebad", 50000, "123-45-6789")

print("Name:", e.name)         # Accessible
print("Salary:", e._salary)    # Accessible (but meant to be protected)

# This line will raise an AttributeError
# print("SSN:", e.__ssn)

# Accessing the private variable using name mangling
print("SSN (via name mangling):", e._Employee__ssn)
