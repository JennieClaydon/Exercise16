from person import Person
# Derived Class - Employee
# Adding some further details - department, pay grade, current task, years service

class Employee(Person):

    def __init__(self, first_name, last_name, age, gender, department, pay_grade, task, years_service):
        super().__init__(first_name, last_name, age, gender)
        self.department = department
        self.pay_grade = pay_grade
        self.task = task
        self.years_service = years_service


    def print_employee_details(self):
        print("Name,", self.first_name, self.last_name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Department:", self.department)
        print("Pay Grade:", self.pay_grade)

    # Method to find what each employee is working on
    def work(self):
        print(self.first_name, self.last_name, "is working on", self.task)

    # Method to work out which employee should be considered for promotion
    def consider_for_promotion(self):
        if self.years_service <= 3:
            print("No")
        if self.years_service > 3:
            print("Yes, more than 3 years service")

