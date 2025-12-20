# Create a class 2D vector and use it to create another class representing a 3D vector

class TwoD_vector:
    def __init__(self, i, j):
        # Initialize 2D vector components
        self.i = i
        self.j = j

    def show(self):
        # Display the 2D vector
        print(f"The 2D vector is {self.i}i + {self.j}j")


# ThreeD_vector inherits from TwoD_vector
class ThreeD_vector(TwoD_vector):
    def __init__(self, i, j, k):
        # Call parent class constructor for i and j
        super().__init__(i, j)
        # Initialize 3D vector component
        self.k = k

    def show(self):
        # Display the 3D vector
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")


# Creating object of TwoD_vector
a = TwoD_vector(1, 2)
a.show()

# Creating object of ThreeD_vector
b = ThreeD_vector(1, 2, 3)
b.show()
