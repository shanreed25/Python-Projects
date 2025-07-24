from turtle import Turtle
import random


# make the Food class Inherit from the Turtle() class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # normally 20px x 20px,
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)#change to 10px x 10px
        self.color("green")
        self.speed("fastest")
        self.move_food()


    def move_food(self):# move the food to a random location
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
