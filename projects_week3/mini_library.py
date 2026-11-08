class Book:
    total_books = 0
    def __init__(self, name, author, copies):
        self.name = name
        self.author = author
        self.copies = copies
        if copies < 1:
            raise ValueError("copies must be at least 1")
        self.available = copies
        Book.total_books += 1


    def borrow(self):
        if self.available == 0:
            raise ValueError("no copies available")
        self.available -= 1

    def return_book(self):
        if self.available == self.copies:
            raise ValueError("all copies are already in")
        self.available += 1

    def is_available(self):
        return True if self.available >= 1 else False

    def __str__(self):
        return f"{self.name} by {self.author} ({self.available}/{self.copies} available) {self.is_available()}"



