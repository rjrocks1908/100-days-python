rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

comp_num = random.randint(0,2)
game_asset = [rock, paper, scissors]

if num >= 0 and num <= 2:
    print(game_asset[num])
    print("Computer Chose:")
    print(game_asset[comp_num])

if num == comp_num:
    print("It's a tie!")
elif num == 0 and comp_num == 1:
    print("Computer wins!")
elif num == 0 and comp_num == 2:
    print("You win!")
elif num == 1 and comp_num == 0:
    print("You win!")
elif num == 1 and comp_num == 2:
    print("Computer wins!")
elif num == 2 and comp_num == 0:
    print("Computer wins!")
elif num == 2 and comp_num == 1:
    print("You win!")
else:
    print("Invalid Input, You lose!")