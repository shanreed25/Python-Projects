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

def get_user_input():
    # TODO-6: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
    first_number = input("Enter first Number:  ")
    user_operation = input("Pick an operation + , -, * or /  ")
    second_number = input("Enter second Number:  ")
    return first_number, user_operation, second_number

def get_cal_function(f_num, user_op, sec_num):
    op_function = None
    for operator in operation_functions:
        if user_op == operator:
            op_function = operation_functions[operator]
    results = op_function(float(f_num), float(sec_num))
    return results

def calculate():
    print(logo)
    user_response = get_user_input()
    calculation_result = get_cal_function(user_response[0], user_response[1], user_response[2])
    print(f"{user_response[0]}  {user_response[1]}  { user_response[2]}")
    print(f"Result: {calculation_result}")
calculate()