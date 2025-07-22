import turtle
from turtle import Turtle, Screen
from random import choice, randint


my_canvas = Screen()
turtle.colormode(255)
spiro = Turtle()
# Create a Spirograph
# draw circles and rotating the turtle's orientation
# draw a series of interconnected circles or arcs, simulating the patterns created by a physical spirograph toy

spiro.speed("fastest")

# the
def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    random_color = (red, green, blue)
    return random_color

def draw_spirograph(degree_for_gap):
    # only need as many circles as it takes to go in a full circle
    # one full circle is 360 degrees
    # you can divide the degree/position/offset by 360 then we will get the correct number
    # of circles it would take to go in a full circle, so there is no overlap
    for _ in range(int(360 / degree_for_gap)):
        spiro.color(get_random_color())
        # Draw circle with radius 100
        spiro.circle(100)
        # heading() refers to the pointing direction
        # spiro.heading() returns the current pointing position
        spiro.setheading(spiro.heading() + degree_for_gap)


draw_spirograph(10)

# # Spirograph - 2
# for _ in range():
#     spiro.color(get_random_color())
#     # Draw circle with radius 100
#     spiro.circle(100)
#     # heading() refers to the pointing direction
#     # spiro.heading() returns the current pointing position
#     spiro.setheading(spiro.heading() + 10)





# Spirograph - 3

#
# for _ in range(100):
#     spiro.color(get_random_color())
#     # Draw circle with a radius 100
#     spiro.circle(100)
#     # turn the turtle 10 degree to the right after drawing each
#     spiro.right(10)

my_canvas.exitonclick()