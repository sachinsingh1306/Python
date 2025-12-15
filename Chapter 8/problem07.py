# Write a program to find out whether a file is identical & matches the content of another file.
with open("Hi-score.txt", "r") as f:
    content1 = f.read()

with open("Hi-score_copy.txt", "r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes It Matches")
else:
    print("No, It does not Matched") 