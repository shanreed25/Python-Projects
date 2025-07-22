import random
from turtle import Turtle, Screen

my_canvas = Screen()
my_canvas.setup(width=500, height=400) 
colors = ["red", "orange", "purple", "yellow", "green", "blue"]

is_race_going = False
user_bet = my_canvas.textinput(title="Make Your Bet",  prompt="Which turtle will win the race? Enter a color: ").lower()

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

print(user_bet)
my_canvas.exitonclick()