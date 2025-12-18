# Create the class program for storing information of few programers working with Microsoft

class Program:
    company = "My organization is Microsoft"
    def __init__(self, name, language, pin):
        self.name = f"My name is {name}.\n"
        self.language = f"I have good command on {language} language.\n"
        self.pin = f"My pin code No. is {pin}.\n"

name = input("Enter your name : ")
language = input("Enter your programming language : ")
pin = int(input("Enter your address pinNO. : "))

p = Program(name, language, pin)
print(p.name, p.language, p.pin, p.company)