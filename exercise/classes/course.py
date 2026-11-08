# class Course:
#     def __init__(self, code, name, contain):
#         self.code = code
#         self.name = name
#         self.contain = contain
#         self.in_course = []
#         self.waitings = []
#
#     def enroll(self, student):
#         self.student = student
#         if self.name in self.in_course or self.name in self.waitings:
#             raise ValueError(f"{self.name} is already registered")
#         elif len(self.in_course) < self.contain:
#             self.in_course.append(self.name)
#             return "enrolled"
#         else:
#             self.waitings.append(self.name)
#             return "waitlisted"
#
#     def __str__(self):
#         return f"{self.code} {self.name} {len(self.in_course)}/{self.contain} {len(self.waitings)}"