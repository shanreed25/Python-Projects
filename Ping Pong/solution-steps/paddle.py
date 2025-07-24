from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        self.position = position
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.position)


    def move_up(self):
        new_ycor = self.ycor() + 20
        self.speed("fastest")
        self.goto(self.xcor(), new_ycor)
        #print(self.xcor())

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.speed("fastest")
        self.goto(self.xcor(), new_ycor)
