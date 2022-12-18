import random
import os
from art import logo, vs
from game_data import data


def get_person(option, person):
    name = person['name']
    description = person['description']
    country = person['country']
    return print(f"Compare {option}: {name}, a {description}, from {country}")


def compare(first_person, second_person):
    person1_followers = first_person['follower_count']
    person2_followers = second_person['follower_count']
    if person1_followers > person2_followers:
        return 'A'
    else:
        return 'B'


def new_game(score):
    os.system('cls')
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")

    first_person = random.choice(data)
    second_person = random.choice(data)
    while first_person == second_person:
        second_person = random.choice(data)

    get_person('A', first_person)
    print(vs)
    get_person('B', second_person)

    chosse = input("Who has more followers? Type 'A' or 'B': ")
    winner = compare(first_person, second_person)

    if winner == chosse:
        return True
    else:
        os.system('cls')
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return False


end_game = False
score = 0
while not end_game:
    win_game = new_game(score)
    if not win_game:
        end_game = True
    else:
        score += 1
