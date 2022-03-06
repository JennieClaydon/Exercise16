from person import Person
# Derived Class - Client - different values on the same original person class

class Client(Person):

    def __init__(self, first_name, last_name, age, gender, loyalty_points, postcode, email_address):
        super().__init__(first_name, last_name, age, gender)
        self.loyalty_points = loyalty_points
        self.postcode = postcode
        self.email_address = email_address

    def print_client_details(self):
        print("Name,", self.first_name, self.last_name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Loyalty Points:", self.loyalty_points)
        print("Postcode:", self.postcode)
        print("Email Address:", self.email_address)

    # Method for working out if they should send a loyalty email based on number of points
    def send_loyalty_email(self):
        if self.loyalty_points >= 200:
            print(self.email_address)


