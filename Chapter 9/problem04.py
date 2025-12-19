# Create a class with a class attribute and a static method

class Demo:
    a = 4   # Class attribute

    @staticmethod
    def hello():
        # Static method does not use self or class variables
        print("Hello World")

o = Demo()        # Create object
print(o.a)        # Access class attribute

o.a = 0           # Create instance attribute
print(o.a)        # Access instance attribute

print(Demo.a)     # Access class attribute

Demo.hello()      # Call static method using class name
o.hello()         # Static method can also be called using object

def Hello():
    print("Hello Sachin !")
Hello()