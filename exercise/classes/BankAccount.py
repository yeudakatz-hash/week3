class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, deposit):
        self._balance += deposit

    def withdraw(self, withdraw):
        if withdraw > self._balance:
            raise ValueError("error: not enough money")
        self._balance -= withdraw

    def get_balance(self):
        return self._balance
