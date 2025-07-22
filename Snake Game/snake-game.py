from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_canvas = Screen()
my_canvas.setup(width=600, height=600)
my_canvas.bgcolor("black")
my_canvas.title("Snake Game")
my_canvas.tracer(0)

my_snake = Snake()
food = Food()

my_canvas.listen()
my_canvas.onkey(fun=my_snake.move_down, key="Down")
my_canvas.onkey(fun=my_snake.move_up,  key="Up")
my_canvas.onkey(fun=my_snake.move_left, key="Left")
my_canvas.onkey(fun=my_snake.move_right, key="Right")

snake_is_moving = True
score = 0 
scoreboard = ScoreBoard()
while snake_is_moving:
    my_canvas.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.move_food()
        scoreboard.update_score()
        my_snake.grow() 
    elif my_snake.head.xcor() < -300 or my_snake.head.ycor() < -290 or my_snake.head.xcor() > 290 or my_snake.head.ycor() > 300:
        scoreboard.game_over()
        snake_is_moving = False

    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard.game_over() 
            snake_is_moving = False

my_canvas.exitonclick()