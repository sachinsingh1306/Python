# Write a class calculator capable of finding square, cube and square root of a number

class Calculator:
    name = "Calculator"

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of {self.n} is {self.n * self.n}")

    def cube(self):
        print(f"Cube of {self.n} is {self.n * self.n * self.n}")

    def square_root(self):
        print(f"Square root of {self.n} is {(self.n ** (1/2))}")

n = int(input("Enter a number: "))
c = Calculator(n)

c.square()
c.cube()
c.square_root()
