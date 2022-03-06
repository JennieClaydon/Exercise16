# Testing that the classes all work

from person import Person
from employees import Employee
from clients import Client

# Person
person_one = Person("John", "Smith", 30, "Male")
person_two = Person("Joe", "Bloggs", 32, "Male")
person_three = Person("Jane", "Mcdonald", 29, "Female")

person_one.printname()
person_one.print_details()
person_two.printname()
person_two.print_details()
person_three.printname()
person_three.print_details()

# Employee
employee_one = Employee("Chris", "Waters", 45, "Male", "Marketing", "7L", "New Branding", 3)
employee_two = Employee("Sarah", "Fisher", 36, "Female", "Finance", "7H", "Pricing for new products", 4)
employee_three = Employee("Claire", "Thomas", 38, "Female", "Operations", "8", "shift 8-8", 2)

employee_one.print_employee_details()
employee_two.print_employee_details()
employee_three.print_employee_details()

# encapsulation
employee_one.work()
employee_two.work()
employee_three.work()


# Client
client_one = Client("Maria", "Jones", 78, "Female", 300, "BH6 7RJ")
client_two = Client("Paul", "Hughes", 80, "Male", 450, "DY78 KL9")
client_three = Client("Samantha", "White", 79, "Female", 67, "HF76 9DR")

client_one.print_client_details()
client_two.print_client_details()
client_three.print_client_details()