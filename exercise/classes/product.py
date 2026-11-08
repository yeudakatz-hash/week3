class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        if price <= 0:
            raise ValueError
        self.quantity = 0


