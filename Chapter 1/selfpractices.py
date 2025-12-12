#Q1. Simple greeting

name = input("Enter your name...")
print(f"Hello {name}, Welcome to Python.")

#Q2. Add two Numbers

a = int(input("Enter number 1st : "))
b = int(input("Enter number 2nd : "))

print("Sum of 1st & 2nd is : ", a+b)

print("Difference of 1st & 2nd is : ", a-b)
print("Product of 1st & 2nd is : ", a*b)
print("Average of 1st & 2nd is : ", (a+b)/2)

#Q3. Temperature Convert (C-> F)

a = float(input("Enter temperature in the degree Celcius : "))

b = (a * 9/5) + 32

print("Temperature in Fehrenheit : ", b)

#Q4. Simple About me Formatter

name = "Sachin Singh"
age = 25
city = "Gorakhpur"

print(f"My name is {name}, I am {age} year old and I live in {city}.")

# Q5. Bonus

name = input("Enter your name :")
birth_year = int(input("Enter your Birth Year :"))
age = 2025 - birth_year

print(f"Hi {name}, you are around {age} years old in 2025.")


# Q6.  Write the Poem 
print('''Twinkel Twinkel Little Star
how are wonder what you are
Like a diamond in the Sky
Twinkel Twinkel Little Star
''')