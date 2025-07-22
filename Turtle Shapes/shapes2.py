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
reed = Turtle()
colors  = [
    "MediumVioletRed","Blue", "OrangeRed", "Purple", "Magenta", "Yellow", "DarkOrchid", "DarkGreen", "DarkOrchid4",
    "CornflowerBlue", "Lime", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray", "SeaGreen"
    ]


# Move from starting position
def move():
    reed.penup()
    reed.goto(-10, 200)
    reed.pendown()

def draw_shape(sides, angle):
    reed.pencolor(choice(colors))
    for _ in range(sides):
        reed.right(angle)
        reed.forward(100)

def draw():
    draw_shape( 3, 120 ) # triangle
    draw_shape( 4, 90 ) # square
    draw_shape( 5, 72 ) # pentagon
    draw_shape( 6, 60 ) # hexagon
    draw_shape( 7, 51.4 ) # heptagon()
    draw_shape( 8, 45 ) # octagon()
    draw_shape( 9, 40 ) # nonagon()
    draw_shape( 10, 36 ) # decagon()

move()
draw()

canvas.exitonclick()