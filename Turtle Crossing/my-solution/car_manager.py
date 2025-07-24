from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5 # move distance on each refresh
# MOVE_INCREMENT = 10 # how much move distance should increase every time the user levels up

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)# 20px high by 40px wide
        self.color(COLORS[random.randint(0, len(COLORS) - 1)])
        self.penup()
        # move to the left edge of the screen
        # No cars should be generated in the top and bottom 50px of the screen
        self.goto(300, random.randint(-250, 250) )# randomly generated along the y-axis
        self.setheading(180)

    def move(self, move_increment):
        new_xcor = self.xcor() - move_increment
        self.goto(new_xcor, self.ycor())

