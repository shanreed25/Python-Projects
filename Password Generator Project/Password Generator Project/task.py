import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


random_letter = letters[random.randint(0, 25)]
random_number = numbers[random.randint(0, 8)]
random_symbol = symbols[random.randint(0, 8)]

# print(random_letter)
# print(random_number)
# print(random_symbol)

print("Welcome to the PyPassword Generator!")
user_letter_count = int(input("How many letters would you like in your password?\n"))
user_symbol_count = int(input(f"How many symbols would you like?\n"))
user_number_count = int(input(f"How many numbers would you like?\n"))
user_password = []
for i in range(user_letter_count):
    random_letter = letters[random.randint(0, 25)]
    user_password.append(random_letter)
    # print(random_letter)

for i in range(user_symbol_count):
    random_symbol = symbols[random.randint(0, 8)]
    user_password.append(random_symbol)
    # print(random_symbol)

for i in range(user_number_count):
    random_number = numbers[random.randint(0, 8)]
    user_password.append(random_number)
    # print(random_number)

print(user_password)
random.shuffle(user_password)
print(user_password)
generated_password = "".join(user_password)
print(f"Password: '{generated_password}'")

###############################OR##################################
# password = ""
#the user letter count need 1 added to it because arrays count start at 0
# for letter in range(1, user_letter_count + 1):
#     # get a random letter from list x(user_letter_count + 1) number of times
#     random_letter = random.choice(letters)
#     # add the letter to the password
#     password = password + random_letter # same as password += random_letter
#     print(password)

####################################################################
# password = ""
# for letter in range(1, user_letter_count + 1):
#     password += random.choice(letters)
#     # print(password)
#
# for number in range(1, user_number_count + 1):
#     password += random.choice(numbers)
#     # print(password)
#
# for symbol in range(1, user_symbol_count + 1):
#     password += random.choice(symbols)
# print(password)
####################################################################
# password = ""
# for letter in range(0, user_letter_count):
#     password += random.choice(letters)
#     # print(password)
#
# for number in range(0, user_number_count):
#     password += random.choice(numbers)
#     # print(password)
#
# for symbol in range(0, user_symbol_count):
#     password += random.choice(symbols)
# print(password)


