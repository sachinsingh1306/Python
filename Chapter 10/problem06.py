# Write a __str__() method to print the vector

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __mul__(self, other):
        return (self.x * other.x +
                self.y * other.y +
                self.z * other.z)

    def __str__(self):   # string representation
        return f"{self.x}i + {self.y}j + {self.z}k"


x = int(input("Value of X : "))
y = int(input("Value of Y : "))
z = int(input("Value of Z : "))

v1 = Vector(x, y, z)
v2 = Vector(x, y, z)
v3 = Vector(x, y, z)

v = v1 + v2 + v3

print(v)   # __str__() is called automatically
print("Dot Product:", v1 * v2)
