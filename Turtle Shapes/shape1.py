from turtle import Turtle, Screen
from random import choice
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# From 3 sided shape to 10 sided shape
# Draw with random colors
# Each side should be 100 in length
# Square has 90 degree angles
# full circle is 360 degrees
# so, 360 / number of sides = angle

canvas = Screen()
lee = Turtle()
colors  = [
    "MediumVioletRed","Blue", "OrangeRed", "Purple", "Magenta", "Yellow", "DarkOrchid", "DarkGreen", "DarkOrchid4",
    "CornflowerBlue", "Lime", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"
    ]

# Move from starting position
def move():
    lee.penup()
    lee.goto(-10, 200)
    lee.pendown()

# function to draw shape
def draw_shape(sides):
    angle = 360/ sides
    for _ in range(sides):
        lee.right(angle)
        lee.forward(100)


move()
# for every shape(number) change the pen color then draw the shape
# will start as 3, then 4, then 5 etc... until 10
for shape in range(3, 11):
    lee.pencolor(choice(colors))
    draw_shape(shape)

canvas.exitonclick()