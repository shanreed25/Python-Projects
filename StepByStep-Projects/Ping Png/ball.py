from turtle import Turtle
# Instructor's Solution*********************************************************************
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        # print(self.x_move, self.y_move)
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)


    def bounce_y(self):
        # change y to go in the opposite direction
        # changes the value of self.y_move to - 10
        # which changes self.y_move in the move function, which add -10 instead of 10
        self.y_move *= -1


    def bounce_x(self):
        # change x to go in the opposite direction
        # changes the value of self.x_move to - 10
        # which changes self.x_move in the move function, which add -10 instead of 10
        self.x_move *= -1

    def reset_ball(self):
        # go to the middle
        self.goto(0, 0)
        # go in the opposite direction
        self.bounce_x()
# My Solution************************************************************************************
# class Ball(Turtle):
#     def __init__(self):
#         self.header = 0
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.shapesize(stretch_wid=1.5, stretch_len=1.5)
#         self.setheading(37)
#
#     def move(self):
#         self.speed(1)
#         self.forward(10)
#         #print(self.position())
#
#     def bounce(self,header):
#         self.setheading(header)
#         self.up_right()




# Solution**********************************************************************************************************
# from turtle import Turtle
# # Instructor's Solution*********************************************************************
# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.shapesize(stretch_wid=1.5, stretch_len=1.5)
#         self.x_move = 10
#         self.y_move = 10
#         # to increase speed of ball
#         # passed to time.sleep()
#         self.ball_move_speed = 0.1

#     def move(self):
#         # print(self.x_move, self.y_move)
#         new_xcor = self.xcor() + self.x_move
#         new_ycor = self.ycor() + self.y_move
#         self.goto(new_xcor, new_ycor)

#     #Touched by top ot bottom walls
#     def bounce_y(self):
#         # change y to go in the opposite direction
#         # changes the value of self.y_move to - 10
#         # which changes self.y_move in the move function, which add -10 instead of 10
#         self.y_move *= -1

#     # Touched by a paddle
#     def bounce_x(self):
#         # change x to go in the opposite direction
#         # changes the value of self.x_move to - 10
#         # which changes self.x_move in the move function, which add -10 instead of 10
#         self.x_move *= -1
#         # Each time the ball hits a paddle it will increase in speed
#         # the ball move speed increase * by decimal number
#         self.ball_move_speed *= 0.9

#     def reset_ball(self):
#         # go to the middle
#         self.goto(0, 0)
#         #sets the ball speed back to original after a player has scored a point
#         self.ball_move_speed = 0.1
#         # go in the opposite direction
#         self.bounce_x()
# # My Solution************************************************************************************
# # class Ball(Turtle):
# #     def __init__(self):
# #         self.header = 0
# #         super().__init__()
# #         self.shape("circle")
# #         self.color("white")
# #         self.penup()
# #         self.shapesize(stretch_wid=1.5, stretch_len=1.5)
# #         self.setheading(37)
# #
# #     def move(self):
# #         self.speed(1)
# #         self.forward(10)
# #         #print(self.position())
# #
# #     def bounce(self,header):
# #         self.setheading(header)
# #         self.up_right()