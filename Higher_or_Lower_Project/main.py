from art import logo, vs
from game_data import data
import random

def game():
    for item in data:
        print(logo)
        compare_a = data[0]
        compare_b = data[1]
        print(f"Compare A: {compare_a['name']},a {compare_a['follower_count']}, from{compare_a['description', 'country']}")
        print (vs)
        print(f"Compare B: {compare_b['name']},a {compare_b['follower_count']}, from{compare_b['description', 'country']}")

game()
