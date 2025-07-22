import turtle
from turtle import Turtle, Screen
from random import choice, randint


canvas = Screen()
lee = Turtle()
lee.color("DeepSkyBlue")

# generate random colors using turtle.colormode()
# to use this we must tap into the turtle module not the Trutle() object
# turtle.colormode()
    # controls how color values are interpreted
    # By default, the turtle module uses a color mode where RGB values are expected
    # to be floating-point numbers between 0.0 and 1.0.(pure red would be (1.0, 0.0, 0.0))
    # you can switch the color mode to use integer values between 0 and 255 (like standard RGB values)
    # by calling turtle.colormode(255): (pure red would be (255, 0, 0))
# Key points:
    # turtle.colormode() without an argument returns the current color mode (either 1.0 or 255).
    # You must call turtle.colormode(255) before you start setting colors using 0-255 integer values.
    # The colormode() function is a method of the Screen object, but it can be called directly from
    # the turtle module as a convenience.
turtle.colormode(255)# from 0 to 255

def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    random_color = (red, green, blue)
    return random_color

# Draw a random walk
# make the line thicker: pensize() or width() method of your turtle object
lee.pensize(15) # sets the line thickness to 15 pixels
# lee.width(15) # sets the line width to 15


# speed up turtle: use the speed() method, can be an integer from 0 to 10
# 1 is slowest, 10 is fastest
# 0 means no animation, drawing instantly
lee.speed(5)
# you can also use a  speedstring
# lee.speed("fastest")


# Random movement north, east, south or west
# In the default "standard" mode of the turtle module
    # turtle start t 0 moving it forward headed east
    # a 90 degree turn changes the direction to north
    # From the setheading() doc: 0(East), 90(North), 180(West), 270(south)
direction = [0, 90, 180, 270]
# choose which direction to go each time

for _ in range(500):
    lee.pencolor(get_random_color())
    # Progress by the same distance each time
    lee.forward(35)
    # setheading(): sets the heading (orientation) of a turtle: Alias: seth()
    # takes an angle as an argument, which represents the new orientation of the turtle in degrees
    lee.setheading(choice(direction))

canvas.exitonclick()