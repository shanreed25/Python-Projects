from art import logo
#
# user_name = input("What's your name?")
# bid = input("What's your bid?")

more_bids = True
#
bids_list = {}
#
def get_user_bid():
    # TODO-1: Ask the user for input
    user_name = input("What's your name?\n")
    bid = float(input("What's your bid?\n"))
    # TODO-2: Save data into dictionary {name: price}
    bids_list[user_name] = bid
    # print(bids_list)

# TODO-4: Compare bids in dictionary
def get_highest_bidder(bids_dic):
    print(logo * 6)
    winner = ""
    highest_bid = 0
    for bidder in bids_dic:
        bid = bids_dic[bidder]
        # print(bids_dic[bidder])
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder
    # for key in bids_dic:
    #     if bids_dic[key] == highest_bid:
    #         winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while more_bids:
    print("\n" * 60)#This will add 100 lines to the output
    print(logo)
    get_user_bid()
    # TODO-3: Whether if new bids need to be added
    another_bid = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if another_bid == 'no':
        more_bids = False
        get_highest_bidder(bids_list)
    elif another_bid == 'yes':
        print("\n" * 60)
        print(logo)









# def get_highest_bidder(bids):
#     max_bid = max(bids.values())
#     for key, value in bids.items():
#         if value == max_bid:
#             print(f"The winner is {key} with a bid of ${value}")
#
# get_highest_bidder(bids_list)


