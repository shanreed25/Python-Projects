from art import logo
import random


# TODO - Function Create a function that  deals the cards
def deal_card():
    """Returns a random card from the deck"""
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards_list)
    return card

# TODO-Function Create a function to calculate the score
def calculate_score(cards):
    # should return the sum of all the cards in the List as the score.
    """
    Check if a hand has two cards that equal 21
    if True returns: 0
    Checks if a hand has an 11 and the score is over 21
    """
    # checks for blackjack whne the players only have two cards
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    # checks if the cards has an 11 and is over 21
    if 11 in cards and sum(cards) > 21:
        # if true remove the 11 for the list and add 1 to the list
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score , c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    # TODO-2 Deal the user and computer 2 cards each using deal_card() and append()
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    is_game_over = False

    # TODO-1 Deal Cards
    # Using range() to run the for loop twice
    # Since we only need the loop to run twice
    # the underscore(_) is used because we do not need a variable
    for _ in range(2):
        # every time the loop runs it will output a random card
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Calculate Score, Check for blackjack, determine if user wants to hit or pass
    while not is_game_over:
        # TODO - 2 Calculate Score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")


        # TODO Check if anyone has Blackjack or has gone over 21
        #if the user has 21 or the computer has 21 or the user score is over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            # if True game over
            is_game_over = True
            # if user_score == 0:
                # print(f"Your cards: {user_cards}, final score: {user_score}")
                # print(f"Computer cards: {computer_cards}, final score: {computer_score}")
                # print("You Win, with Blackjack!! 😃")

        # TODO Determine if user want to hit or pass
        else:
            # ask the user if they want to hit(y) or pass(n)
            user_should_hit = input("Type 'y' to hit, type 'n' to pass:")
            if user_should_hit == "y":
                # deal the user another card
                user_cards.append(deal_card())
            else:
                is_game_over = True


    # At this point user has selected to pass
    # we need to deal the computer cards
    # TODO Deal computer cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)



    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    # At this point user and computer are done getting cards
    #we need to compare the user score and the computer score
    print(compare(user_score, computer_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
