from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time


# TODO-5 Detect when paddle misses the ball

# Screen**********************************************************
# TODO-1 Create Table(Screen())
my_canvas = Screen()
my_canvas.setup(width=800, height=600)
my_canvas.title("Pong")
my_canvas.bgcolor("black")
my_canvas.listen()
my_canvas.tracer(0)

# Table Divider Turtle*********************************************
table_divider = Turtle()
table_divider.color("white")
table_divider.setheading(90)
table_divider.penup()
table_divider.goto(x=0, y=-490)

# Player 1 Paddle**************************************************
# TODO-2 Create Player 1 Paddle and make it move
player1_paddle = Paddle((-380, 0))
my_canvas.onkey(fun=player1_paddle.move_up, key="q")
my_canvas.onkey(fun=player1_paddle.move_down, key="a")

# Player 1 Paddle**************************************************
# TODO-3 Create Player 2 Paddle and make it move
player2_paddle = Paddle((380, 0))
my_canvas.onkey(fun=player2_paddle.move_up, key="Up")
my_canvas.onkey(fun=player2_paddle.move_down, key="Down")


# TODO-4 Create Ball and Make it move
ball = Ball()


# TODO-5 Keep Score
scoreboard = ScoreBoard()

def add_table_divider():
    while table_divider.ycor() < 600:
        table_divider.pendown()
        table_divider.forward(20)
        table_divider.penup()
        table_divider.forward(20)

add_table_divider()

game_going = True
while game_going:
    time.sleep(ball.ball_move_speed)
    my_canvas.update()
    # TODO-4 Create Ball and Make it move
    ball.move()

    # TODO-5 Detect Collision with wall and bounce back

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # TODO-6 Detect Collision with paddle and bounce back
    if ball.distance(player2_paddle) < 50 and ball.xcor() > 340 or ball.distance(player1_paddle) < 50 and ball.xcor() < -340 :
        ball.bounce_x()

    # TODO-5 Detect when paddle misses the ball
    if ball.xcor() > 350:
        scoreboard.l_point()
        ball.reset_ball()

    if ball.xcor() < - 350:
        scoreboard.r_point()
        ball.reset_ball()



my_canvas.exitonclick()