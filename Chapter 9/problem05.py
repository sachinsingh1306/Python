# Write a class Train which has methods to:
# book a ticket, get status (number of seats / running status),
# and get fare information of trains running under Indian Railways

from random import randint   # Import randint to generate random fare

class Train:
    def __init__(self, TrainNo):
        # Constructor to initialize train number
        self.TrainNo = TrainNo

    def Book(self, fro, to):
        # Method to book a ticket from source to destination
        print(f"Ticket is booked in TrainNo : {self.TrainNo} from {fro} to {to}.")

    def getStatus(self):
        # Method to show train running status
        print(f"TrainNo : {self.TrainNo} is running on time.")

    def getFare(self, fro, to):
        # Method to display ticket fare (random value for demo)
        print(
            f"Ticket fare in TrainNo : {self.TrainNo} "
            f"from {fro} to {to} is ₹{randint(250, 999)}"
        )

# Taking user input for journey details
fro = input("Enter name of Station From : ")
to = input("Enter name of Station To : ")

# Creating object of Train class
detail = Train(15053)

# Calling class methods
detail.Book(fro, to)
detail.getStatus()
detail.getFare(fro, to)
