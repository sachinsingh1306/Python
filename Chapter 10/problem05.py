# Create a class Vector representing a vector of n dimension
# Overload + for addition and * for dot product

class Vector:
    def __init__(self, x, y, z):   # accept values properly
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):      # vector addition
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __mul__(self, other):      # dot product
        return (self.x * other.x +
                self.y * other.y +
                self.z * other.z)

    def show(self):
        print(f"{self.x}i + {self.y}j + {self.z}k")


x = int(input("Value of X :"))
y = int(input("Value of Y :"))
z = int(input("Value of X :"))


v1 = Vector(x,y,z)
v2 = Vector(x,y,z)
v3 = Vector(x,y,z)

v = v1 + v2 + v3
v.show()

print("Dot Product:", v1 * v2)
