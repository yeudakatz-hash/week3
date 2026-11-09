from shop_product import Product

class Inventory:
    def __init__(self):
        self._products = []

    def add(self, new_product):
        if new_product in self._products:
            raise ValueError("already exists")
        self._products.append(new_product)

    def find(self, name_product):
        for product in self._products:
            if name_product == product.name:
                return product
        return None

    def total_value(self):
        return sum(product.total_value for product in self._products)

    def by_value(self):
        return sorted(self._products, key=lambda p:p.total_value)

