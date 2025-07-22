MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine_on = True
cash = 0.0

def complete_transaction(coffee_choice):
    print("Please Insert Coins")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01

    payment = quarters + dimes + nickles + pennies
    global cash


    if payment > MENU[coffee_choice]['cost']:
        change = round(payment - MENU[coffee_choice]['cost'], 2)
        cash += round(MENU[coffee_choice]['cost'], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_choice} enjoy ")
    else:
        print(f"Your payment was not enough to get a {coffee_choice}, Money refunded ")
    return payment

def check_user_choice_resources(coffee_choice):

    def check_resources(current_resource, coffee_type, needed_resource):
        if resources[current_resource] >= MENU[coffee_type]['ingredients'][needed_resource]:
            resources[current_resource] -= MENU[coffee_type]['ingredients'][needed_resource]
            return True
        else:
            return False

    if coffee_choice == 'latte' or coffee_choice == 'cappuccino':
        if check_resources('water', user_choice, 'water'):
            if check_resources('milk', user_choice, 'milk'):
                if check_resources('coffee', user_choice, 'coffee'):
                    complete_transaction(coffee_choice)
                else:
                    print('Sorry there is not enough coffee')
            else:
                print('Sorry there is not enough milk')
        else:
            print('Sorry there is not enough water')

    if coffee_choice == 'espresso':
        if check_resources('water', user_choice, 'water'):
            if check_resources('coffee', user_choice, 'coffee'):
                payment = complete_transaction(coffee_choice)
                return payment
            else:
                print('Sorry there is not enough coffee')
        else:
            print('Sorry there is not enough water')

while coffee_machine_on:
    # once the drink is dispensed, prompt should show again to serve the next customer
    #  Prompt user
    # Check the user’s input to decide what to do next

    user_choice = input("What would you like? 'espresso' 'latte' 'cappuccino':  ").lower()

    # show the current resources when user enters "report"
    # TODO-1 Print report
    if user_choice == 'report':
        for key in resources:
            if key == 'water' or key == 'milk':
                print(f"{key.capitalize()}: {resources[key]}ml")
            elif key == 'coffee':
                print(f"{key.capitalize()}: {resources[key]}g")
        print(f"Money: ${cash} ")

    # TODO-2 turn off machine
    # Turn off the Coffee Machine by entering “off” to the prompt
    if user_choice == 'off':
        print("Turning Off.....")
        coffee_machine_on = False

    # TODO-3 check for sufficient resources
    check_user_choice_resources(user_choice)