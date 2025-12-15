# 8. Write a program to make a copy of a text file "Hi-score.txt"

with open("Hi-score.txt", "r") as f:
    content = f.read()

with open("Hi-score_copy.txt", "w") as f:
    f.write(content)

print("Program Run ")