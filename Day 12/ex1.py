import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(guess, answer, guess_attemps):
    if guess > answer:
        print("Too High.")
    elif guess < answer:
        print("Too Low.")
    elif guess == answer:
        print(f"You got it! the answer was {answer}.")
        return True, 0

    guess_attemps -= 1
    if guess_attemps == 0:
        print("You've run out of guesses, you lose.")
        return True, 0
    else:
        print("Guess again.")

    return False, guess_attemps


def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level == "easy":
            return EASY_LEVEL
        elif level == "hard":
            return HARD_LEVEL
        else:
            print("Type only 'easy' or 'hard'")


def start_game():
    answer = random.randint(1, 100)
    print(logo)
    print("I'm thinking of a number between 1 and 100")

    guess_attemps = set_difficulty()

    got_answer = False
    while not got_answer:
        print(
            f"You have {guess_attemps} attemps remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        got_answer, guess_attemps = check_answer(
            guess_number, answer, guess_attemps)

    replay = input("Do you want play another one? y/n:")
    if replay == "y":
        start_game()


start_game()
