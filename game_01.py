'''
Docstring for game_01
It is a Snake Water Gun game
1  is for Snake
-1 is for Water
0 is for Gun

Game Between Computer VS You/User
'''

import random  # Import random module for computer choice

# Game instructions
print("S means Snake \nW means Water\nG means Gun  \nStart Game !!!")

# Computer randomly selects Snake, Water, or Gun
computer = random.choice([-1, 0, 1])

# Take user input and convert to lowercase
youStr = input("Enter your Choice : ").lower()

# Dictionary to map user input to game values
youDict = {"s": 1, "w": -1, "g": 0}

# Dictionary to convert values back to readable form
reversedDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Validate user input
if youStr not in youDict:
    print("Invalid choice! Please enter S, W, or G.")
else:
    # Convert user choice to numeric value
    you = youDict[youStr]

    # Display choices
    print(f"Your Choice {reversedDict[you]}\nComputer Choice {reversedDict[computer]}")

    # Game logic
    if computer == you:
        print("Its Draw !")
    elif computer == 1 and you == 0:
        print("You Win !")
    elif computer == 1 and you == -1:
        print("You Lose !")
    elif computer == -1 and you == 1:
        print("You Win !")
    elif computer == -1 and you == 0:
        print("You Lose !")
    elif computer == 0 and you == 1:
        print("You Lose !")
    elif computer == 0 and you == -1:
        print("You Win !")
    else:
        print("Something Went Wrong Try Again.")


# Shortest Way to do same logic is 

if youStr not in youDict:
    print("Invalid choice! Please enter S, W, or G.")
else:
    # Convert user choice to numeric value
    you = youDict[youStr]

    if computer == you:
        print("Draw")
    elif (computer - you) == -2 or (computer - you) == 1:
        print("Win")
    else:
        print("Lose")

