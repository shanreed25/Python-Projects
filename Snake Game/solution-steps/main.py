from turtle import Screen
from snake_1 import Snake
from food_1 import Food
from scoreboard import ScoreBoard
import time

# Put Food on screen

# Create Score Board
# Write some text that tells us when the score has increased
# Score should increase when the snake head hit a new piece of food
# Turtle can write using turtle.write()
# arg = what it should write, align = "what kind of alignment you want the text to be"
# font = (font of text)



# Detect collision with wall
my_canvas = Screen()
my_canvas.setup(width=600, height=600)
my_canvas.bgcolor("black")
my_canvas.title("Snake Game")
my_canvas.tracer(0)

# Create Snake Body
my_snake = Snake()
# Put Food on screen
food = Food()




# Control Snake
my_canvas.listen()
my_canvas.onkey(fun=my_snake.move_down, key="Down")
my_canvas.onkey(fun=my_snake.move_up,  key="Up")
my_canvas.onkey(fun=my_snake.move_left, key="Left")
my_canvas.onkey(fun=my_snake.move_right, key="Right")


# Move Snake
snake_is_moving = True
score = 0 # starting score
scoreboard = ScoreBoard()
while snake_is_moving:
    my_canvas.update()
    time.sleep(0.1)
    my_snake.move()


       # Detect collision with food
    if my_snake.head.distance(food) < 15:
        food.move_food()
        scoreboard.update_score()
        my_snake.grow() # grow snake
    # Detect collision with wall
    elif my_snake.head.xcor() < -300 or my_snake.head.ycor() < -290 or my_snake.head.xcor() > 290 or my_snake.head.ycor() > 300:
        scoreboard.reset_scoreboard() # snake has collided with wall
        my_snake.reset_snake()

    # Detect collision with tail
    for segment in my_snake.segments[1:]:# using slicing
        # if segment == my_snake.head: # used slicing to remove this
        #     pass # if the segment is the snake head, do nothing
        if my_snake.head.distance(segment) < 10:# if the segment is less than 10px away from any other segments
            scoreboard.reset_scoreboard() # snake has collided with body 
            my_snake.reset_snake()
            











my_canvas.exitonclick()