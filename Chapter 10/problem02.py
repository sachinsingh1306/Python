# Create a class Animals, then Pets, then Dog with a bark method

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow !!")

# Create object and call method
d = Dog()
d.bark()
