from clients import Client
# Running to get a list of email addresses of customers who have enough loyalty points for email
client_one = Client("Maria", "Jones", 78, "Female", 300, "BH6 7RJ", "maria.jones@gmail.com")
client_two = Client("Paul", "Hughes", 80, "Male", 450, "DY78 KL9", "paulh@hotmail.com")
client_three = Client("Samantha", "White", 79, "Female", 67, "HF76 9DR", "samanthajwhite@gmail.com")
client_four = Client("", "", "", "", 600, "", "test@hotmail.com")

# question - can you run the below syntax without listing all the customer details above - ie can you import the data
# that is stored somewhere else?

print("Send loyalty emails to:")

client_one.send_loyalty_email()
client_two.send_loyalty_email()
client_three.send_loyalty_email()
client_four.send_loyalty_email()
