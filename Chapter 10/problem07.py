# Vector class with __len__() method on vector of 5 to display the dimension of the vector

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

    def __len__(self):
        return 3   # 3D vector


x = int(input("Value of X : "))
y = int(input("Value of Y : "))
z = int(input("Value of Z : "))

v1 = Vector(x, y, z)
v2 = Vector(x, y, z)
v3 = Vector(x, y, z)

v = v1 + v2 + v3

print("Length of vector:", len(v))
