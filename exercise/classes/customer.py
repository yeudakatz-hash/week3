class Customers:
    def __init__(self, name, city):
        self.name = name
        self.city = city


class Order:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

