import turtle
import random

# Create Spot Painting
# 10 x 10 rows of spots
# each spot should be 20 in diameter
# space apart by 50


# set color mode
turtle.colormode(255)

my_canvas = turtle.Screen()
dot_turtle = turtle.Turtle()
color_list = [(95, 251, 160), (175, 148, 120), (229, 45, 185), (153, 107, 64), (7, 4, 175), (249, 149, 188), (226, 251, 105), (144, 62, 240), (12, 85, 169), (236, 10, 228), (44, 243, 46), (35, 35, 249), (12, 209, 206), (241, 4, 2), (250, 150, 146), (247, 74, 69), (232, 5, 15), (83, 249, 253), (6, 210, 216), (226, 127, 192), (3, 2, 106), (138, 149, 213), (173, 162, 245), (207, 118, 30), (254, 3, 6), (252, 7, 5)]
dot_turtle.speed("fastest")
dot_turtle.penup()
dot_turtle.hideturtle()


# # Other Solution***************************************************************
# dot_turtle.setheading(225)
# dot_turtle.forward(300)
# dot_turtle.setheading(0)
# num_of_dots = 100
#
# for dot_count in range(1, num_of_dots + 1):
#     dot_turtle.dot(20, random.choice(color_list))
#     dot_turtle.forward(50)
#
#     if dot_count % 10 == 0:
#         dot_turtle.setheading(90)
#         dot_turtle.forward(50)
#         dot_turtle.setheading(180)
#         dot_turtle.forward(500)
#         dot_turtle.setheading(0)

# my solution******************************************************************
x_axis = 180
y_axis = -200
def create_spot_painting(x, y):
    for _ in range(10):
        for _ in range(10):
            dot_turtle.goto(x, y)
            # Draw Dot
            dot_turtle.dot(30, random.choice(color_list))
            x -= 50
        x = 180
        y += 50


create_spot_painting(x_axis, y_axis)
my_canvas.exitonclick()