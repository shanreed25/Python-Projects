from game_data import data
from art import logo
from art import vs
import random




def getdata(account_data):
    """Takes account data and returns the data in f string"""
    account_name = account_data['name']
    account_description = account_data['description']
    account_country = account_data['country']
    account_followers = account_data['follower_count']
    person_info = f" {account_name}, a {account_description}, from {account_country} {account_followers}"
    return person_info

# print logo
print(logo)
#get a random option from data
# TODO-1 Get a random person from the data
option_b = random.choice(data)
print(option_b)

# variable for game to continue
continue_game = True
# variable for score
score = 0


while continue_game:
    # Option B should become option A every time the game continues
    option_a = option_b
    option_b = random.choice(data)

    if option_a['follower_count'] == option_b['follower_count']:
        option_b = random.choice(data)
    # TODO-2 Print the name, description, and country of each person
    print(f"Compare A: {getdata(option_a)}.")
    print(vs)
    print(f"Against B: {getdata(option_b)}.")

# TODO-3 Get the user choice
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == 'a':
        if option_a['follower_count'] > option_b['follower_count']:
            score +=1
            print(f"You're right! Current score: {score} ")
            continue_game = True
        elif option_a['follower_count'] < option_b['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False
    elif user_choice == 'b':
        if option_b['follower_count'] > option_a['follower_count']:
            score += 1
            print(f"You're right! Current score: {score} ")
            continue_game = True
        elif option_b['follower_count'] < option_a['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False
    else:
        print(f"Sorry, you must enter 'a' or 'b'. Final score: {score}")
        continue_game = False
