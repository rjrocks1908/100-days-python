import art
from game_data import data
import random
import os

dataLen = len(data)
score = 0
NAME = "name"
FOLLOWER_COUNT = "follower_count"
DESCRIPTION = "description"
COUNTRY = "country"


def generateRandomData():
    return data[random.randint(0, dataLen - 1)]


def getResults(candA, candB, userInput):
    global score
    if userInput == "A":
        if candA[FOLLOWER_COUNT] > candB[FOLLOWER_COUNT]:
            score += 1
            return True
        else:
            return False
    elif userInput == "B":
        if candA[FOLLOWER_COUNT] < candB[FOLLOWER_COUNT]:
            score += 1
            return True
        else:
            return False


def game():
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    candA = generateRandomData()
    candB = generateRandomData()
    while candA == candB:
        candB = generateRandomData()

    print(f"Compare A: {candA[NAME]}, a {candA[DESCRIPTION]}, from {candA[COUNTRY]}\n")

    print(art.vs)

    print(f"Against B: {candB[NAME]}, a {candB[DESCRIPTION]}, from {candB[COUNTRY]}")

    userInput = input("Who has more followers? Type 'A' or 'B': ")
    return getResults(candA, candB, userInput)


while True:
    if game():
        os.system("cls")
        continue
    else:
        os.system("cls")
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        break
