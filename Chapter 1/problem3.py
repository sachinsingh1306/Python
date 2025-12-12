a = input("Enter any value: ")

# check for integer
if a.isdigit():
    print("Type of", a, "is int")

# check for float
elif a.replace('.', '', 1).isdigit():
    print("Type of", a, "is float")

# otherwise it's string
else:
    print("Type of", a, "is string")
