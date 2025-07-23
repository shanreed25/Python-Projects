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





# My Solution******************************************************************************
# class Paddle(Turtle):
#     def __init__(self, position):
#         # self.segments = []
#         self.position = position
#         super().__init__()
#         self.shape("square")
#         self.shapesize(stretch_len=5)
#         self.color("white")
#         self.setheading(90)
#         self.penup()
#         self.goto(self.position)
#
#
#     def move_up(self):
#         self.forward(20)
#         self.speed("fastest")
#
#     def move_down(self):
#         self.backward(20)
#         self.speed("fastest")
#


    #     self.create_paddle()
    #
    # def create_paddle(self):
    #     for position in self.positions:
    #         new_segment = Turtle()
    #         new_segment.shape("square")
    #         new_segment.shapesize(stretch_wid=1.5)
    #         new_segment.color("white")
    #         new_segment.penup()
    #         new_segment.goto(position)
    #         self.segments.append(new_segment)