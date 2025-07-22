from art import logo
# TODO-1: Create function that adds two numbers
def add(n1, n2):
    return n1 + n2
# TODO-2: Create function that subtracts two numbers
def subtract(n1, n2):
    return n1 - n2
# TODO-3: Create function that multiplies two numbers
def multiply(n1, n2):
    return n1 * n2
# TODO-4: Create function that divides two numbers
def divide(n1, n2):
    return n1 / n2

# TODO-5: Add these 4 functions into a dictionary as the values. Keys = "`+`", "`-`", "`*`", "`/`"
operation_functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


# do_more = True
# first_number = float(input("Enter first Number:  "))
# while do_more:
#     for key in operation_functions:
#         print(key)
#     user_operation = input("Pick an operation ")
#     second_number = float(input("Enter second Number:  "))
#     result = operation_functions[user_operation](first_number, second_number)
#     print(f"{first_number} {user_operation} {second_number} = {result}")
#     continue_working = input(f"Type 'y' to continue with {result}, or type 'n' to start new calculation").lower()
#     if continue_working == 'y':
#         first_number = result
#         print(result)
#     else:
#         print("goodbye")
#         do_more = False
#         print("\n" * 20)
#**************************************************************************************

## Instead of using two while loops we can use Recursion
# keep_calculating = True
# while keep_calculating:
#     print(logo)
#     do_more = True
#     first_number = float(input("Enter first Number:  "))
#     while do_more:
#         for key in operation_functions:
#             print(key)
#         user_operation = input("Pick an operation ")
#         second_number = float(input("Enter second Number:  "))
#         result = operation_functions[user_operation](first_number, second_number)
#         print(f"{first_number} {user_operation} {second_number} = {result}")
#         continue_working = input(f"Type 'y' to continue with {result}, or type 'n' to start new calculation").lower()
#         if continue_working == 'y':
#             first_number = result
#             print(result)
#         else:
#             print("goodbye")
#             do_more = False
#             print("\n" * 30)


def calculate():
    print(logo)
    do_more = True
    first_number = float(input("Enter first Number:  "))
    while do_more:
        for key in operation_functions:
            print(key)
        user_operation = input("Pick an operation ")
        second_number = float(input("Enter second Number:  "))
        result = operation_functions[user_operation](first_number, second_number)
        print(f"{first_number} {user_operation} {second_number} = {result}")
        continue_working = input(f"Type 'y' to continue with {result}, or type 'n' to start new calculation").lower()
        if continue_working == 'y':
            first_number = result
            print(result)
        else:
            print("goodbye")
            do_more = False
            print("\n" * 20)
            # calling this function inside itself is called recursion
            calculate()
calculate()