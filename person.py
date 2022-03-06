# Base Class - Person

class Person:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def printname(self):
        print("Name:", self.first_name, self.last_name)

    def print_details(self):
        print("Age:", self.age)
        print("Gender:", self.gender)


