from turtle import Screen
from snake_1 import Snake
from food_1 import Food




import time
# Control Snake
# Put Food on screen
# Detect collision with food
# Create Score Board
# Detect collision with wall
my_canvas = Screen()
my_canvas.setup(width=600, height=600)
my_canvas.bgcolor("black")
my_canvas.title("Snake Game")
my_canvas.tracer(0)

# Create Snake Body: Code moved into Snake class snake_1.py
my_snake = Snake()

# Move Snake Up, Down, Left Right: Code created in Snake class snake_1.py
my_canvas.listen()
my_canvas.onkey(fun=my_snake.move_down, key="Down")
my_canvas.onkey(fun=my_snake.move_up,  key="Up")
my_canvas.onkey(fun=my_snake.move_left, key="Left")
my_canvas.onkey(fun=my_snake.move_right, key="Right")



# Put Food on screen
food = Food()

snake_is_moving = True
while snake_is_moving:
    my_canvas.update()
    time.sleep(0.1)
    my_snake.move()



    # Detect collision with food
    # using distance method: works by comparing the distance from the turtle to whatever
    # it is that you pass into the method: turtle.distance(x, y)
    # x can be a number or a pair/vector of numbers or a turtle
    # y should be a number if x is a number otherwise none
    # the food is 10px x 10px, so we will add a buffer of 5px totaling 15px
    # Detect collision with food
    if my_snake.head.distance(food) < 15: # if the snake head is less than 15px from the food
        print("Yumm, Yumm Yummy")
        food.move_food()

my_canvas.exitonclick()