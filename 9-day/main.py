import os
from art import logo
print(logo)
print("Welcome to the secret auction program.")

bidders = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    
    bidders[name] = bid
    
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if choice == "no":
        break
    else:
        os.system('cls')

highestBid = 0
winner = ""
for bidder, bid in bidders.items():
    if bid > highestBid:
        highestBid = bid
        winner = bidder

os.system('cls')
print(f"The winner is {winner} with a bid of ${highestBid}.")