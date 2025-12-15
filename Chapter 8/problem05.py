# Write a program to mine a log file and find out whether it contains 'python'.

with open("frist.txt", "r") as f:
    lines = f.readlines()
    lineNo = 1
    for line in lines:
        if "python" in line.lower():
            print(f"Yes, {lineNo}")
            # break
        lineNo += 1
    else:
        print("No")
