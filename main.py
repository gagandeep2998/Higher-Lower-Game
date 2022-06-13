from game_data import data
from art import logo, vs
import random


def get_random_account():
    random_account = random.choice(data)
    return random_account


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, {description}, {country}"


def check_followers(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True

    a_account = get_random_account()
    b_account = get_random_account()

    while game_should_continue:
        while a_account == b_account:
            b_account = get_random_account()

        print(f"Compare A: {format_data(a_account)}.")
        print(vs)
        print(f"Against B: {format_data(b_account)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = a_account["follower_count"]
        b_follower_count = b_account["follower_count"]

        is_correct = check_followers(guess, a_follower_count, b_follower_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You're right, current score: {score}")
            a_account = b_account
            b_account = get_random_account()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong answer, Final score: {score}")


game()





