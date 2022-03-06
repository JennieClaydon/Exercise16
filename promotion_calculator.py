from employees import Employee
# Promotion calculator
employee_one = Employee("Chris", "Waters", 45, "Male", "Marketing", "7L", "New Branding", 3)
employee_two = Employee("Sarah", "Fisher", 36, "Female", "Finance", "7H", "Pricing for new products", 4)
employee_three = Employee("Claire", "Thomas", 38, "Female", "Operations", "8", "shift 8-8", 2)

# question - can you run the below syntax without listing all the customer details above - ie can you import the data
# that is stored somewhere else?

print("Due to be considered for a Promotion?")

employee_one.printname()
employee_one.consider_for_promotion()

employee_two.printname()
employee_two.consider_for_promotion()

employee_three.printname()
employee_three.consider_for_promotion()