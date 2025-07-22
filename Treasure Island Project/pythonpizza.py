print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")

# extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0
if size == "S":
    price = 15
elif size == "M":
    price = 20
elif size == "L":
    price = 25
else:
    print("Please choose S, M, or L")
    exit()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" and size == "S":
    price += 2
if pepperoni == "Y" and size == "M" or pepperoni == "Y" and size == "L":
    price += 3
else:
    price = price

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    price += 1
else:
    price = price
print(f"Your final bill is: ${price}.")



# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# if pepperoni == "Y":
#     if size == "S": # Nested if Statement
#         price += 2
#     if size == "M":
#         price += 3
#     if size == "L":
#         price += 3
#     else:
#         print("Please choose Y or N")
#         exit()
# else:
#     price = price
