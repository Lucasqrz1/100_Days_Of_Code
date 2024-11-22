from art import logo, vs
from game_data import data
import random


def get_random_data():
    return random.choice(data)

def format_data(item):
    return f"{item['name']}, a {item['description']}, from {item['country']}"

def game():
    print(logo)
    score = 0
    game_continues = True

    compare_a = get_random_data()
    compare_b = get_random_data()

    while compare_a == compare_b:
        compare_b =get_random_data()

    while game_continues:
        compare_a = compare_b
        compare_b = get_random_data()

        compare_a = get_random_data()
        compare_b = get_random_data()
        print(f"Compare A: {format_data(compare_a)}")
        print(vs)
        print(f"Compare B: {format_data(compare_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_follower_count = compare_a['follower_count']
        b_follower_count = compare_b['follower_count']

        is_correct = (guess == 'A' and a_follower_count > b_follower_count)



game()
