from classes.person import Person
from classes.product import Product
from classes.student import Student
from classes.shop_products import ProductShop


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

