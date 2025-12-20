class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r}r + {self.i}i"


# Dynamic input
r1 = int(input("Enter real part of first complex number: "))
i1 = int(input("Enter imaginary part of first complex number: "))

r2 = int(input("Enter real part of second complex number: "))
i2 = int(input("Enter imaginary part of second complex number: "))

c1 = Complex(r1, i1)
c2 = Complex(r2, i2)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
