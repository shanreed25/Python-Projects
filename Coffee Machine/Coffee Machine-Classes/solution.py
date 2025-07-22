from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()



coffee_machine_on = True
while coffee_machine_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? {options}:  ").lower()
    if user_choice == 'report': # Print Report
        coffee_maker.report()
        money_machine.report()
    elif user_choice == 'off': # turn off machine
        print("Turning Off.....")
        coffee_machine_on = False
    else:
        # drink = menu.find_drink(user_choice)
        # if coffee_maker.is_resource_sufficient(drink):
        #     if money_machine.make_payment(drink.cost):
        #         coffee_maker.make_coffee(drink)
        # or
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)