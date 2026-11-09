from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, max_kg):
        super().__init__(brand, 6)
        self.max_kg = max_kg
        self.load_kg = 0

    def load(self, weight):
        if self.load_kg + weight > self.max_kg:
            raise ValueError(f"overloaded: max {self.max_kg} kg")
        self.load_kg += weight