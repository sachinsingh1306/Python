# Repeat program 4 for a list of such words to be censored.
list = ["python", "sachin", "alok"]
with open("frist.txt", "r") as f:
    content = f.read().lower()

    for word in list:
        if(word in content):
         print("Yes")
        else:
         print("No")