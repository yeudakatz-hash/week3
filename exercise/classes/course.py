class Course:
    def __init__(self, code, name, contain):
        self.code = code
        self.name = name
        self.contain = contain
        self.in_course = []
        self.waitings = []

    def enroll(self, student):
        if student in self.in_course or student in self.waitings:
            raise ValueError(f"{student} is already registered")
        elif len(self.in_course) < self.contain:
            self.in_course.append(student)
            return "enrolled"
        self.waitings.append(student)
        return "waitlisted"

    def __str__(self):
        return f"{self.code} {self.name} {len(self.in_course)}/{self.contain} waitlist:{len(self.waitings)}"