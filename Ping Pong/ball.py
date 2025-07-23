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
        self.ball_move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.ball_move_speed = 0.1
        self.bounce_x()
