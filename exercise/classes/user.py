class User:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if 0 < value < 120:
            self._age = value
        else:
            raise ValueError("age must be 0-120")
