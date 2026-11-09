class PaymentMethod:
    def __init__(self, pay):
        self.pay = pay

    @property
    def pay(self):
        return self.pay

    @pay.setter
    def pay(self, new_value):
        raise NotImplementedError
