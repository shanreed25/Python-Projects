from turtle import Turtle

STARTING_POSITION = (0, -280) # Bottom of the screen
MOVE_DISTANCE = 10 # how much the turtle move each time
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def start_again(self):
        self.goto(STARTING_POSITION)# return the turtle to the starting position
