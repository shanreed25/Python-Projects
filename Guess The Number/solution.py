import random
from art import logo
from random import randint


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")



# TODO  Get a random number 1-100
number_to_guess = random.choice(range(1, 101))
#******or
# number_to_guess = randint(1, 100)
print(number_to_guess)


HARD_LEVEL = 5
EASY_LEVEL = 10



def choose_level():
    num_of_tries = 0
    # TODO Ask the user to choose a difficulty level
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        num_of_tries = EASY_LEVEL
        return num_of_tries
    elif difficulty == 'hard':
        num_of_tries = HARD_LEVEL
        return num_of_tries
    else:
        print("You must type 'easy' or 'hard")
        choose_level()


def play_game(tries):
    print(f"You have {tries} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == number_to_guess:
        print(f"You got it! The answer was {number_to_guess}")
    elif user_guess > number_to_guess:
        tries -= 1
        if tries == 0:
            print("You've run out of guesses. Refresh the page to run again.")
        else:
            print("Too High")
            print("Guess again.")
            play_game(tries)
    elif user_guess < number_to_guess:
        tries -= 1
        if tries == 0:
            print("You've run out of guesses. Refresh the page to run again.")
        else:
            print("Too Low")
            print("Guess again.")
            play_game(tries)
    else:
        print("error")

user_tries = choose_level()
play_game(user_tries)
