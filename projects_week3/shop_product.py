class Product:
    def __init__(self, name, price, quantity = 0):
        self._name = name
        self.price = price
        self._quantity = quantity


    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self._price = value


    def add_stock(self, new_inventory):
        if new_inventory <= 0:
            raise ValueError
        self._quantity += new_inventory

    def sell(self, quant):
        if quant <= 0:
            raise ValueError
        if quant > self._quantity:
            raise ValueError("Not enough stock available")
        self._quantity -= quant

    @property
    def total_value(self):
        return self.price * self._quantity

    def __eq__(self, other):
        if isinstance(other, Product):
            return self._name == other._name
        return False

    def __str__(self):
        return f"{self._name}: {self._quantity} * {self.price} = {self.total_value}"
