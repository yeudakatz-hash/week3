class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def __str__(self):
        return self.name + " (average " + str(self.average()) + ")"

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        try:
            return sum(self.grades) / len(self.grades)
        except:
            return 0
