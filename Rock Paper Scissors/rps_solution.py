import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#1st Option
#computer_choice = random.randint(0, 2)
# print(rock)

#2nd Option
choice_list = [rock, paper, scissors]
computer_choice = random.choice(choice_list)
computer_choice_index = choice_list.index(computer_choice)

# Get User choice
user_choice_index = int((input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n ")))
if user_choice_index > 3 or user_choice_index < 0:
    print('You must type 0 for Rock, 1 for Paper, or 2 for Scissors ')
    exit()
# print(computer_choice_index)
# print(user_choice_index)
user_choice = choice_list[user_choice_index]
# print(user_choice)
# print(f"You Chose:\n{user_choice}\nComputer Chose {computer_choice}")
#

if computer_choice_index == 0 and user_choice_index == 1:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nYou Win!!!!!")
elif computer_choice_index == 0 and user_choice_index == 2:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nYou Lose!!!!!")
elif computer_choice_index == 0 and user_choice_index == 0:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nIt's a Draw!!!!!")
elif computer_choice_index == 1 and user_choice_index == 1:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nIt's a Draw!!!!!")
elif computer_choice_index == 1 and user_choice_index == 2:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nYou Win!!!!!")
elif computer_choice_index == 1 and user_choice_index == 0:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nYou Lose!!!!!")
elif computer_choice_index == 2 and user_choice_index == 2:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nIt's A Draw!!!!!")
elif computer_choice_index == 2 and user_choice_index == 0:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nYou Win!!!!!")
elif computer_choice_index == 2 and user_choice_index == 1:
    print(f"Computer Chose: {computer_choice}\nYou Chose: {user_choice}\nYou Lose!!!!!")


















