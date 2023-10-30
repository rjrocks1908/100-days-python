from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100")
chosenNumber = random.randint(1, 100)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def checkAnswer(guess):
    if guess < chosenNumber:
        print("Too low.")
    elif guess > chosenNumber:
        print("Too high.")
    else:
        print(f"You got it! The number was {chosenNumber}.")
        return True
    return False

def setDifficulty():
    if input("Choose a difficulty: Type 'easy' or 'hard': ") == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def startGame():
    win = False
    attempts = setDifficulty()
    
    for attempt in range(attempts):
        print(f"You have {attempts-attempt} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        win = checkAnswer(guess = guess)
        if not win:
            print("Guess again.")
        else:
            break
    
    if not win:
        print("You've run out of guesses, you lose.")

startGame()