from .emp import Emp

class Man(Emp):
    def __init__(self, name,salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_cost(self):
        return super().monthly_cost() + self.bonus