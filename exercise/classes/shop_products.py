


class ProductShop:

    VAT_RATE = 0.17
    count_product = 0

    def __init__(self, name, price):


        self.name = name
        self.price = price
        ProductShop.count_product += 1

    def price_with_vat(self):
        return self.price * (1 + ProductShop.VAT_RATE)



