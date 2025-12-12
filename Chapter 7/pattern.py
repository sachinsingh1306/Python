n = int(input("Enter a  number..."))

def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n-1)

pattern(n)

# Convert inches to cm
inch = int(input("Enter an inch: "))

def inch_to_cm(inch_value):
    return inch_value * 2.54

print(inch_to_cm(inch))
