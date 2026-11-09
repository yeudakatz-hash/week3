from mini_library import Book
from shop_product import Product
from shop_inventory import Inventory

books = [
    Book("Clean Code", "Martin", 3),
    Book("Python Basics", "Cohen", 1),
]

books[0].borrow()
books[1].borrow()

try:
    books[1].borrow()
except ValueError as error:
    print("Python Basics ->", error)

try:
    Book("Empty", "Nobody", 0)
except ValueError as error:
    print("Empty ->", error)

for book in books:
    print(book, "| available:", book.is_available())

print("Books in the library:", Book.total_books)






shop = Inventory()
shop.add(Product("pen", 5, 10))
shop.add(Product("bag", 60, 2))
shop.add(Product("Notebook", 12, 5))
shop.find("pen").sell(4)
shop.find("bag").add_stock(1)

try:
    shop.find("Notebook").sell(50)
except ValueError as error:
    print("error", error)
try:
    shop.add(Product("pen", 7))
except ValueError as error:
    print("error", error)
try:
    shop.find("bag").price = -3
except ValueError as error:
    print("error", error)
for product in shop.by_value():
    print(product)
    print("total", shop.total_value())