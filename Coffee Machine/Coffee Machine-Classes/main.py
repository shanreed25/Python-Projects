from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
drink_menu = Menu()
my_coffee_machine = CoffeeMaker()
# print(my_coffee_machine.is_resource_sufficient(drink_menu.find_drink('latte')))

#latte
latte = drink_menu.menu[0]
latte_cost = drink_menu.menu[0].cost
# can_make_latte = my_coffee_machine.is_resource_sufficient(drink_menu.menu[0])
can_make_latte = my_coffee_machine.is_resource_sufficient(drink_menu.find_drink('latte'))

#espresso
espresso = drink_menu.menu[1]
espresso_cost = drink_menu.menu[1].cost
can_make_espresso = my_coffee_machine.is_resource_sufficient(drink_menu.menu[1])

#cappuccino
cappuccino = drink_menu.menu[2]
cappuccino_cost = drink_menu.menu[2].cost
can_make_cappuccino = my_coffee_machine.is_resource_sufficient(drink_menu.menu[2])

process_payment = my_money_machine.make_payment


coffee_machine_on = True
while coffee_machine_on:
    user_choice = input("What would you like? 'espresso' 'latte' 'cappuccino':  ").lower()

    # show the current resources when user enters "report"
    # TODO-1 Print report
    if user_choice == 'report':
        my_coffee_machine.report()
        my_money_machine.report()

        # TODO-2 turn off machine
        # Turn off the Coffee Machine by entering “off” to the prompt
    if user_choice == 'off':
        print("Turning Off.....")
        coffee_machine_on = False

    # TODO-3 check for sufficient resources
    if user_choice == 'espresso':
        if can_make_espresso:
            if process_payment(espresso_cost):
                my_coffee_machine.make_coffee(espresso)
    elif user_choice == 'latte':
        if can_make_latte:
            if process_payment(latte_cost):
                my_coffee_machine.make_coffee(latte)
    elif user_choice == 'cappuccino':
        if can_make_cappuccino:
            if process_payment(cappuccino_cost):
                my_coffee_machine.make_coffee(cappuccino)

