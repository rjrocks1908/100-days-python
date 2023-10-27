import random
from art import logo
import os

cardsValue = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def assignCards(myCards, computerCards):
    for _ in range(2):
        myCards.append(random.choice(cardsValue))
        computerCards.append(random.choice(cardsValue))

def calculateScore(cards):
    if 11 in myCards and sum(cards) > 21:
        myCards.remove(11)
        myCards.append(1)
    
    return sum(cards)

while True:
    os.system('cls')
    print(logo)
    myCards = []
    computerCards = []
    assignCards(myCards, computerCards)

    mysum = sum(myCards)
    compSum = sum(computerCards)

    myTurn = True
    while myTurn:
        print(f"Your cards: {myCards}, current score: {mysum}")
        print(f"Computer's first card: {computerCards[0]}")

        if mysum > 21:
            break

        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            myCards.append(random.choice(cardsValue))
        else:
            myTurn = False

        mysum = calculateScore(myCards)
        

    while compSum < 17:
        computerCards.append(random.choice(cardsValue))
        compSum = calculateScore(computerCards)

    print(f"Your final hand: {myCards}, final score: {mysum}")
    print(f"Computer's final hand: {computerCards}, final score: {compSum}")

    if mysum > 21:
        print("You went over. You lose 😭")
    elif compSum > 21:
        print("You win 😃")
    elif mysum > compSum:
        print("You win 😃")
    elif mysum < compSum:
        print("You lose 😤")
    else:
        print("Draw 🙃")

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
        break