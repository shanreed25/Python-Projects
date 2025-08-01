
from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
"""
check_answer() Explanation:
if a_followers > b_followers::
This line checks if the number of followers for entity "a" is greater than the number of followers for entity "b."
return user_guess == "a":
If the condition in the if statement is true (meaning "a" has more followers), this line is executed. It returns True if the user_guess variable is equal to the string "a" (indicating the user correctly guessed that "a" has more followers), and False otherwise.
else::
This keyword indicates an alternative action to be taken if the if condition is false.
return user_guess == "b":
If the if condition is false (meaning "b" has more followers, or they have an equal number), this line is executed. It returns True if the user_guess variable is equal to the string "b" (indicating the user correctly guessed that "b" has more followers), and False otherwise.
In essence, this code determines if the user_guess matches the entity with the higher number of followers, returning True for a correct guess and False for an incorrect guess.
"""


print(logo)
score = 0
game_should_continue = True
# Generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:

    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # - Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False


