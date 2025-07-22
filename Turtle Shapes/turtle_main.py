from turtle import Turtle, Screen
from random import choice


# Graphical User Interface(GUI)
# tkinter is the package that the turtle module relies on (under the hood) to create the graphics



# Screen(object) represents the window in which the turtle is going to show up
canvas = Screen()
# screen(object) attributes
print(canvas.canvheight)# 300


# Create an object from a blueprint that somebody else has already created, from the turtle module
willy = Turtle()

willy.shape("turtle")

print(willy) # <turtle.Turtle object at 0x00000174D918F890>: <turtle object at location on computer>

# Draw a square*********************************************************************************************
# tai = Turtle()
# tai.shape("turtle")
# tai.color("purple")
#
# for _ in range(4):
#     tai.forward(100)
#     tai.right(90)

# Draw dashed line********************************************************************************************
# reed = Turtle()
# reed.shape("turtle")
# reed.color("OliveDrab1")
# reed.pencolor("black")
# reed.penup()
# reed.goto(-350, 200)
# reed.pendown()
# for _ in range(50):
#     reed.forward(5)
#     reed.penup()
#     reed.forward(5)
#     reed.pendown()




# Has to be done after everything else with the turtle
canvas.exitonclick()# will only exit when the screen is clicked


# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors

# import prettytable
# from prettytable import PrettyTable # has to be installed
# table = PrettyTable()

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])

# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_rows(
#     [
#         ["Adelaide", 1295, 1158259, 600.5],
#         ["Brisbane", 5905, 1857594, 1146.4],
#         ["Darwin", 112, 120900, 1714.7],
#         ["Hobart", 1357, 205556, 619.5],
#         ["Sydney", 2058, 4336374, 1214.8],
#         ["Melbourne", 1566, 3806092, 646.9],
#         ["Perth", 5386, 1554769, 869.4],
#     ]
# )
# print(table)

# my_table = PrettyTable()
# # method
# my_table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander" ])
# my_table.add_column("Type",["Electric", "Water", "Fire" ])
#
# # attribute
# print(my_table.align)
# my_table.align = "l"
# print(my_table.align)
#
#
# print(my_table)














