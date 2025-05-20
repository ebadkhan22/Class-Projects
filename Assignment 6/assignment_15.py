class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        print("B's show")

class C(A):
    def show(self):
        print("C's show")

class D(B, C):
    pass

d = D()
d.show()

print("MRO:", [cls.__name__ for cls in D.__mro__])
