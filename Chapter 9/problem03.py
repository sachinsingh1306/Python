# Create a class with a class attribute 'a'

class Demo:
    a = 4          # Class attribute (shared by all objects)

o = Demo()         # Create an object of Demo
print(o.a)         # Access class attribute using object (prints 4)

o.a = 0            # Create an instance attribute 'a' for object o
print(o.a)         # Access instance attribute (prints 0)

print(Demo.a)      # Access class attribute directly (still 4)
