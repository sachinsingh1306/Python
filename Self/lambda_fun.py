'''
# 1. Lambda Function
# Normal Function

n = int(input("Enter a number :"))

# def square(n):
#     return n*n

square = lambda n: n*n
print(square(n))

'''

# 2. Lambda with multiple argument 

add = lambda a, b : a+b
print(add(3,4))


🔹 3. List Comprehension (Very Important)
Normal Way
even_numbers = []
for num in [1, 2, 3, 4, 5, 6]:
    if num % 2 == 0:
        even_numbers.append(num)


List Comprehension Way
even_numbers = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(even_numbers)



🔹 4. List Comprehension with Strings
names = ["Sachin", "Rohan", "Amit", "Sunil"]

upper_names = [name.upper() for name in names]
print(upper_names)