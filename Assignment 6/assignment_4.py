class Bank:
    bank_name = "Default Bank"

    def __init__(self, customer):
        self.customer = customer

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show(self):
        print(self.customer, "->", Bank.bank_name)

a = Bank("Ebad")
b = Bank("Khan")

a.show()
b.show()

Bank.change_bank_name("Global Bank")

a.show()
b.show()
