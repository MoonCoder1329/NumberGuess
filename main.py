import random

from art import logo

print(logo)

def choose_number():
    number = random.randint(1,100)
    return number

result = choose_number()
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number betwwen 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level =="easy":
    easy = True
    while easy:
        for remainder in range (10,0,-1):
            print(f"You have {remainder} attempts remaining to guess the number.")
            guess = int(input("make a guess: "))
            if result > guess:
                print("Too low.")
            if result < guess:
                print("too hight.")
            elif result == guess:
                print(f"You got it! The answer was {result}")
                break
            if remainder >1:
                print("Guess again")
            else:
                print("You've run out of guesses, you lose")
                break

        easy = False
elif level == "hard":
    hard = True
    while hard:
        for remainder in range(5, 0, -1):
            print(f"You have {remainder} attempts remaining to guess the number.")
            guess = int(input("make a guess: "))
            if result > guess:
                print("Too low.")
            if result < guess:
                print("too hight.")
            elif result == guess:
                print(f"You got it! The answer was {result}")
                break
            if remainder > 1:
                print("Guess again")
            else:
                print("You've run out of guesses, you lose")
                print(f"The number is: {result}")
                break

        hard = False
else:
    print("Wrong answer program closed")