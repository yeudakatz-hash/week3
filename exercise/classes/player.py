class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, point):
        self.points += point

    def __str__(self):
        return f"{self.name}: {self.points}"

