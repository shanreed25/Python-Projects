from turtle import Turtle, Screen
# Create a Etch A Sketch
# W = Forwards
# S = Backwards
# A = Counter-Clockwise(left)
# D = Clockwise(right)
# C = Clear Drawing

my_canvas = Screen()
etch_sketch = Turtle()

my_canvas.listen()

def move_forward():
    etch_sketch.forward(20)

# def move_left():
#     etch_sketch.left(20)
#     etch_sketch.heading()
#OR
def move_left():
    new_heading = etch_sketch.heading() + 10
    etch_sketch.setheading(new_heading)

# def move_right():
#     etch_sketch.right(20)
#OR
def move_right():
    new_heading = etch_sketch.heading() - 10
    etch_sketch.setheading(new_heading)

def move_backwards():
    etch_sketch.backward(20)

def clear_sketch():
    etch_sketch.clear() #clear the screeen
    etch_sketch.penup()
    etch_sketch.home() # move the turtle to its initial position and orientation
    etch_sketch.pendown()

my_canvas.onkey(fun=move_forward, key="w")
my_canvas.onkey(fun=move_left, key="a")
my_canvas.onkey(fun=move_right, key="d")
my_canvas.onkey(fun=move_backwards, key="s")
my_canvas.onkey(fun=clear_sketch, key="c")



my_canvas.exitonclick()