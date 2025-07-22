import random
from turtle import Turtle, Screen


# Create Turtle Race
my_canvas = Screen()
my_canvas.setup(width=500, height=400) #set the size and position of the main window
colors = ["red", "orange", "purple", "yellow", "green", "blue"]
# my_canvas.numinput()# need user to enter number

is_race_going = False
user_bet = my_canvas.textinput(title="Make Your Bet",  prompt="Which turtle will win the race? Enter a color: ").lower()# need user to enter text

# Solution 1****************************************************************************************************
def create_turtle(turtle_name, color_num, x, y):
    turtle_name = Turtle(shape="turtle")
    turtle_name.color(colors[color_num])
    turtle_name.penup()
    turtle_name.goto(x, y)
    return turtle_name

turtle_list = [
create_turtle("tai", 0 ,  -230 , -100  ),
create_turtle("ivory", 1 ,  -230 , -60  ),
create_turtle("gracie", 2 ,  -230 , -20  ),
create_turtle("lily", 3 ,  -230 , 20 ),
create_turtle("creed", 4,  -230 , 60  ),
create_turtle("bj", 5 ,  -230 , 100 )
]

if user_bet:
    is_race_going = True

while is_race_going:
    for turtle in turtle_list:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
                is_race_going = False
                winner = turtle.pencolor()
                if user_bet == winner:
                    print(f"You have won!!! The {winner} turtle won!!!!")
                else:
                    print(f"You bet on {user_bet} and lost!!! The {winner} turtle won!!!!")


# Solution 2**************************************************************************************************************
# y_positions= [-100, -60, -20, 20, 60, 100]
# turtle_list = []
# for turtle_index in range(0, 6):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.color(colors[turtle_index])
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=y_positions[turtle_index])
#     turtle_list.append(new_turtle)
#
#
# if user_bet:
#     is_race_going = True
# turtle_speed = random.randint(0,10)
#
# while is_race_going:
#     for turtle in turtle_list:
#         if turtle.xcor() > 230:
#             is_race_going = False
#             winner = turtle.pencolor()
#             if user_bet == winner:
#                 print(f"You have won!!! The {winner} turtle won!!!!")
#             else:
#                 print(f"You bet on {user_bet} and lost!!! The {winner} turtle won!!!!")
#
#
#         turtle.forward(random.randint(0,10))
#
#         # the width is 500 so if the reach 250 they are at the end
#         # but the turtle object is a 40px X 40px object
#         # so if we use 250 that is too far
#         # so to get the turtle to the finish line we have to subtract half the width of the turtle
#         # 250 - (40 /2) = 230
#
#
#
#


print(user_bet)
my_canvas.exitonclick()