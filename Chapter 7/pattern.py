# n = int(input("Enter a  number..."))

# def pattern(n):
#     if n == 0:
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(n)

# # Convert inches to cm
# inch = int(input("Enter an inch: "))

# def inch_to_cm(inch_value):
#     return inch_value * 2.54

# print(inch_to_cm(inch))


# Q7. Remove words from the list and strip it at the same?

# def remove(list, word):
#     n = []
#     for item in list:
#         if not (item == word):
#             n.append(item.strip(word))
#     return n

# list = ["Harry", "Sachin", "Rohan", "an", "Alok"]

# print(remove(list, "ry"))


# Q8. Multiplication 

def multiplication(n):
    for i in range(1,11):
     print(f"{n} X {i} = {n*i}")

multiplication(5)