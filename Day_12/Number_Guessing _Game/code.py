import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
#guess = " "
number = random.randint(1,100)
attempts = " "

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

while attempts > 0:
    guess = int(input(f"You have {attempts} attempts left. Make a guess: "))
    if guess > number:
        print("Too High. Try again")
        attempts -= 1
    elif guess < number:
        print("Too low. Try again.")
        attempts -= 1
    elif guess == number:
        print("Game over! You win.")
    elif attempts == 0:
        print("You ran out of attempts. Game over.")
