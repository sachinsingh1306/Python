# The Prefect Guess Game 

import random
n = random.randint(1, 100)

number = -1
guesses = 1

while(number != n):
    number = int(input("Guess the Number : "))
    if(number< n):
        print("Higher Number Please")
        guesses += 1
    elif(number>n):
        print("Lower Number Please")
        guesses += 1
print(f"You have guessed the number {number} correctly in {guesses} attempts.")