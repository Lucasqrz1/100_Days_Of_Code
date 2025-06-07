import random
from itertools import combinations_with_replacement

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

game_images = [rock, paper, scissors]
user_choice = (int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
)))
computer_choice = (random.randint(0,2))
print(game_images[user_choice])
print("Computer chose")
print(game_images[computer_choice])


if user_choice >2 or user_choice <0:
    print("You type the wrong number! You lose.")
elif user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 2 and computer_choice == 0:
    print("You lost :( ")
elif computer_choice == 2 and user_choice == 0:
    print ("You win!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You lose")
