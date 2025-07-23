from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time
# PONG
# Arcade Game
# A ball going across a table and two players each control a paddle
# Bouncing the ball back and forth
# if you miss, a ball then the other player scores a point







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
# my_canvas.onkey(fun=ball.up_right, key="f")

# TODO-5 Keep Score
# ScoreBoard
player1_score = ScoreBoard((-50, 280))
player2_score = ScoreBoard((50, 280))



# (351.40,264.80)

def add_table_divider():
    while table_divider.ycor() < 600:
        table_divider.pendown()
        table_divider.forward(20)
        table_divider.penup()
        table_divider.forward(20)

add_table_divider()

# my_canvas.update()

# INSTRUTOR"S SOLUTION*********************************************************
game_going = True
while game_going:
    time.sleep(.09)
    my_canvas.update()
    # TODO-4 Create Ball and Make it move
    # Both x cor and y cor increase
    ball.move()

    # x decrease y increase
    # TODO-5 Detect Collision with wall and bounce back
    # Detect collision with wall:******************************************************
    # The height of the screen is 600
    # Top Wall: if the ball is at a y position that is greater than 285 it is too far up
        # collision with top wall: both x and y will be 10
            # x cor should continue to increase: 10
            # the y cor needs to start decreasing: -10
    #  Bottom Wall: or if the ball is at a y position that is less than -285 it is too far down
        # collision with bottom wall: both x and y will be -10
            # x cor should continue decreasing: -10
            # the y cor needs to start increasing: 10
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
        # print(f"bouncey + {ball.position()}")

    # TODO-6 Detect Collision with paddle and bounce back
    # Detect collision with paddles: change x cors*****************************************************************
    # ball.distance(paddle): ball has a width of 20px and paddle has a width of 20px
    # using if ball.distance(paddle) < 20:
        # ball.distance(paddle) measures the center of the ball to the center of the paddle
        # but the ball may not hit the paddle in the middle, and the distance will not be larger than 20px
    # so we could check
        # if the ball is within 50px distance to the paddle
        # and  has gone pass a certain point on the x axis

    # Collision with paddle2(right): if ball distance to paddle2 is less than 50 and ball xcor is greater than 350
        # x cor should start decreasing: -10
        # the y cor needs to start decreasing: 10
    # Collision with paddle1(left): or if ball distance to paddle1 less than 50 and ball xcor is less than -340
        # x cor should start decreasing: -10
        # the y cor needs to start decreasing: -10
    if ball.distance(player2_paddle) < 50 and ball.xcor() > 340 or ball.distance(player1_paddle) < 50 and ball.xcor() < -340 :
        ball.bounce_x()
        # print(f"bouncex + {ball.position()}")
    elif ball.xcor() > 350:
        player1_score.score_point()
        ball.reset_ball()
        print(ball.position())
        print(f"Player 1: {player1_score.score}")
    elif ball.xcor() < - 350:
        player2_score.score_point()
        ball.reset_ball()
        print(f"Player 2: {player2_score.score}")





# MY Solution*******************************************************************
# game_going = True
# while game_going:
#     my_canvas.update()
#     ball.move()
#     time.sleep(.05)
#     print(ball.ycor())
#     if ball.ycor() > 285:
#         ball.bounce(270)
#     if ball.ycor() < -285:
#         ball.bounce(90)



my_canvas.exitonclick()

# Solution(ball.py:bottom, scoreboard.py: bottom************************************************************************
# from turtle import Turtle, Screen
# from paddle import Paddle
# from scoreboard import ScoreBoard
# from ball import Ball
# import time
# # PONG
# # Arcade Game
# # A ball going across a table and two players each control a paddle
# # Bouncing the ball back and forth
# # if you miss, a ball then the other player scores a point

# # TODO-5 Detect when paddle misses the ball

# # Screen**********************************************************
# # TODO-1 Create Table(Screen())
# my_canvas = Screen()
# my_canvas.setup(width=800, height=600)
# my_canvas.title("Pong")
# my_canvas.bgcolor("black")
# my_canvas.listen()
# my_canvas.tracer(0)

# # Table Divider Turtle*********************************************
# table_divider = Turtle()
# table_divider.color("white")
# table_divider.setheading(90)
# table_divider.penup()
# table_divider.goto(x=0, y=-490)

# # Player 1 Paddle**************************************************
# # TODO-2 Create Player 1 Paddle and make it move
# player1_paddle = Paddle((-380, 0))
# my_canvas.onkey(fun=player1_paddle.move_up, key="q")
# my_canvas.onkey(fun=player1_paddle.move_down, key="a")

# # Player 1 Paddle**************************************************
# # TODO-3 Create Player 2 Paddle and make it move
# player2_paddle = Paddle((380, 0))
# my_canvas.onkey(fun=player2_paddle.move_up, key="Up")
# my_canvas.onkey(fun=player2_paddle.move_down, key="Down")


# # TODO-4 Create Ball and Make it move
# ball = Ball()
# # my_canvas.onkey(fun=ball.up_right, key="f")

# # TODO-5 Keep Score
# # ScoreBoard
# scoreboard = ScoreBoard()



# # (351.40,264.80)

# def add_table_divider():
#     while table_divider.ycor() < 600:
#         table_divider.pendown()
#         table_divider.forward(20)
#         table_divider.penup()
#         table_divider.forward(20)

# add_table_divider()

# # my_canvas.update()

# # INSTRUTOR"S SOLUTION*********************************************************
# game_going = True
# while game_going:
#     time.sleep(ball.ball_move_speed)
#     my_canvas.update()
#     # TODO-4 Create Ball and Make it move
#     # Both x cor and y cor increase
#     ball.move()

#     # x decrease y increase
#     # TODO-5 Detect Collision with wall and bounce back
#     # Detect collision with wall:******************************************************
#     # The height of the screen is 600
#     # Top Wall: if the ball is at a y position that is greater than 285 it is too far up
#         # collision with top wall: both x and y will be 10
#             # x cor should continue to increase: 10
#             # the y cor needs to start decreasing: -10
#     #  Bottom Wall: or if the ball is at a y position that is less than -285 it is too far down
#         # collision with bottom wall: both x and y will be -10
#             # x cor should continue decreasing: -10
#             # the y cor needs to start increasing: 10
#     if ball.ycor() > 285 or ball.ycor() < -285:
#         ball.bounce_y()
#         # print(f"bouncey + {ball.position()}")

#     # TODO-6 Detect Collision with paddle and bounce back
#     # Detect collision with paddles: change x cors*****************************************************************
#     # ball.distance(paddle): ball has a width of 20px and paddle has a width of 20px
#     # using if ball.distance(paddle) < 20:
#         # ball.distance(paddle) measures the center of the ball to the center of the paddle
#         # but the ball may not hit the paddle in the middle, and the distance will not be larger than 20px
#     # so we could check
#         # if the ball is within 50px distance to the paddle
#         # and  has gone pass a certain point on the x axis

#     # Collision with paddle2(right): if ball distance to paddle2 is less than 50 and ball xcor is greater than 350
#         # x cor should start decreasing: -10
#         # the y cor needs to start decreasing: 10
#     # Collision with paddle1(left): or if ball distance to paddle1 less than 50 and ball xcor is less than -340
#         # x cor should start decreasing: -10
#         # the y cor needs to start decreasing: -10
#     if ball.distance(player2_paddle) < 50 and ball.xcor() > 340 or ball.distance(player1_paddle) < 50 and ball.xcor() < -340 :
#         ball.bounce_x()

#     # TODO-5 Detect when paddle misses the ball
#     if ball.xcor() > 350:
#         scoreboard.l_point()
#         ball.reset_ball()

#     if ball.xcor() < - 350:
#         scoreboard.r_point()
#         ball.reset_ball()





# # MY Solution*******************************************************************
# # game_going = True
# # while game_going:
# #     my_canvas.update()
# #     ball.move()
# #     time.sleep(.05)
# #     print(ball.ycor())
# #     if ball.ycor() > 285:
# #         ball.bounce(270)
# #     if ball.ycor() < -285:
# #         ball.bounce(90)



# my_canvas.exitonclick()