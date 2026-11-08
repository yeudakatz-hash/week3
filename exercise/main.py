from classes.person import Person
from classes.product import Product
from classes.student import Student
from classes.shop_products import ProductShop
from classes.player import Player
from classes.customer import Customers, Order
from classes.BankAccount import BankAccount
from classes.user import User
from classes.course import Course



dana = Person("Dana" , 24 , "hgtrdcv@gtrf")
avi = Person("Avi" , 20 , "tredfgtrdfg@fgtf")
print(dana.name)




pen =  Product("pen", 5)
print(pen.quantity)
print(pen.price)
print(pen.name)




dana = Student("dana")
print(dana.name)
print(dana.average())
dana.add_grade(90)
dana.add_grade(20)
print(dana.average())
print(dana)




laptop = ProductShop("laptop", 1000)
mouse = ProductShop("mouse", 50)
print(ProductShop.count_product)
print(laptop.price_with_vat())




players = [Player("Dana"), Player("Avi"), Player("Noa")]
players[0].add_points(50)
players[1].add_points(15)
players[2].add_points(40)
players[1].add_points(40)

max_point = 0
winner_name = None
for player in players:
   if player.points > max_point:
       max_point = player.points
       winner_name = player.name
print(winner_name, max_point)




Dana = Customers("Dana", "tel aviv")
Avi = Customers("Avi", "haifa")
order1 = Order(Dana, 120)
order2 = Order(Dana, 20)
print(order1.customer.city)




account = BankAccount("Dana", 100)
account.deposit(50)
try:
    account.withdraw(500)
except ValueError as error:
    print("error:", error)
print(account.get_balance())




user = User(30)
user.age = user.age + 1
print(user.age)
try:
    user.age = -5
except ValueError as error:
    print("error:", error)
print(user.age)



# course = Course("PY101", "Intro To Python", 2)
# for student in ["Dana", "Avi", "Noa"]:
#     print(student, course.enroll(student))
# print(course)
# try:
#     course.enroll("Dana")
# except ValueError as error:
#     print("error:", error)
