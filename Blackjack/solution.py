from art import logo
import random

# Cards List
cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def start_function(function_name):
    function_name()

def check_11(score):
    """
    If an ace is drawn, count it as 11. But if the total
     goes over 21, count the ace as 1 instead
    :param score:
    :return:
    """
    # get new card
    new_card = random.choice(cards_list)
    if new_card == 11: #if the new card is 11
        if new_card + score > 21:#if the new card plus the players score is greater than 21
            new_card = 1 #the new card is changed to 1
        return new_card #return the new card as 1
    else:
        return new_card #if the new card is not 11 return the new card as is


def hit_player(user_score, user_cards, op_score, op_cards):
    """
    handles the user turn when they want to hit
    :param user_score:
    :param user_cards:
    :param op_score:
    :param op_cards:
    :return:
    """
    new_card = check_11(user_score)
    user_cards.append(new_card)
    user_score = sum(user_cards)
    if user_score > 21:
        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer cards: {op_cards}, final score: {op_score}")
        print("You went over. You lose!! 😭")
        start_function(start_game)
    elif user_score < 21:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {op_cards[0]}")
        play(user_score, op_score, user_cards, op_cards)
    elif user_score == 21:
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {op_cards[0]}")
        print("You Win, with Blackjack!! 😃")
        start_function(start_game)
    else:
        print(f"Error: {user_score}, {op_score}")

def find_winner(user_score, user_cards, op_score, op_cards):
    """
    Compare user and computer scores and see if it's a win, loss, or draw
    :param user_score:
    :param user_cards:
    :param op_score:
    :param op_cards:
    :return:
    """
    if user_score == op_score:  # user == op: draw
        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer cards: {op_cards}, final score: {op_score}")
        print("Its A Draw 🙃!!!!")
        start_function(start_game)
    elif user_score > op_score and user_score <= 21:  # user gt op and user lt= 21: User win
        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer cards: {op_cards}, final score: {op_score}")
        print("You Win!! 😃")
        start_function(start_game)
    elif user_score > op_score and user_score > 21:  # user gt op and user gt 21: Op win
        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer cards: {op_cards}, final score: {op_score}")
        print("You went over, You Lose! 😭")
        start_function(start_game)
    elif user_score < op_score and op_score > 21:  # user lt op and op gt 21: User win
        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer cards: {op_cards}, final score: {op_score}")
        print("Computer went over, You Win! 😃")
        start_function(start_game)
    elif user_score < op_score and op_score <= 21:  # user lt op and op lt= 21: Op win
        print(f"Your cards: {user_cards}, final score: {user_score}")
        print(f"Computer cards: {op_cards}, final score: {op_score}")
        print("You Lose! 😭")
        start_function(start_game)
    else:
        print("Some Error")


def computer_go(user_score, user_cards, op_score, op_cards):
    """
    Handles the computer's turn
    :param user_score:
    :param user_cards:
    :param op_score:
    :param op_cards:
    :return:
    """
    while op_score <= 16:
        new_card = check_11(op_score)
        op_cards.append(new_card)
        op_score = sum(op_cards)
    print(f"Op cards: {op_cards}")
    print(f"Op score: {op_score}")

    find_winner(user_score, user_cards, op_score, op_cards)


def play(user_score, op_score, user_cards, op_cards):
    '''
    Checks if the player wants to hit or pass
    :param user_score:
    :param op_score:
    :param user_cards:
    :param op_cards:
    :return:
    '''
    hit = input("Type 'y' to get another card, type 'n' to pass:")
    if hit == 'y':
        hit_player(user_score, user_cards, op_score, op_cards)
    elif hit == 'n':
        computer_go(user_score, user_cards, op_score, op_cards)
    else:
        print("You must enter 'y' or 'n' ")
        play(user_score, op_score, user_cards, op_cards)


def check_score(cards):
    '''
    Checks to see if  the starting hand has 2 11s
    :param cards:
    :return:
    '''
    if sum(cards) == 22:
        cards[1] = 1
    return cards

#***************************************************************************************
def start_game():
    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
    # Deal both user and computer a starting hand of 2 random card values.
    player_cards = [random.choice(cards_list), random.choice(cards_list)]
    computer_cards = [random.choice(cards_list), random.choice(cards_list)]

    player_cards = check_score(player_cards)
    computer_cards = check_score(computer_cards)
    # Calculate the user's and computer's scores based on their card values.
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)


    if play_blackjack == 'y':
        print(logo)

        # TODO Show the player their cards and tell them their score
        print(f"Your cards: {player_cards}, current score: {player_score}")

        # TODO Show the player the computer's first card
        print(f"Computer first card: {computer_cards[0]}")

        # TODO- 2 Detect when computer or user has a blackjack. (Ace + 10 value card).
        if computer_score == 21:  # If computer gets blackjack, then the user loses
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer cards: {computer_cards}, current score: {computer_score}")
            print("You Lose 😭")
            start_function(start_game())
        elif player_score == 21:  # If the user gets a blackjack, then they win (unless the computer also has a blackjack)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer cards: {computer_cards}, current score: {computer_score}")
            print("You Win, with Blackjack!!!! 😃")
            start_function(start_game())
        else:
            play(player_score, computer_score, player_cards, computer_cards)
    elif play_blackjack == 'n':
        print("Thanks for playing....Goodbye")
    else:
        start_game()

# TODO Ask user to play blackjack

start_game()
