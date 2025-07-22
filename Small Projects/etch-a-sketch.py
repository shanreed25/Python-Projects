from turtle import Turtle, Screen

my_canvas = Screen()
etch_sketch = Turtle()

my_canvas.listen()

def move_forward():
    etch_sketch.forward(20)

def move_left():
    new_heading = etch_sketch.heading() + 10
    etch_sketch.setheading(new_heading)

def move_right():
    new_heading = etch_sketch.heading() - 10
    etch_sketch.setheading(new_heading)

def move_backwards():
    etch_sketch.backward(20)

def clear_sketch():
    etch_sketch.clear()
    etch_sketch.penup()
    etch_sketch.home()
    etch_sketch.pendown()

my_canvas.onkey(fun=move_forward, key="w")
my_canvas.onkey(fun=move_left, key="a")
my_canvas.onkey(fun=move_right, key="d")
my_canvas.onkey(fun=move_backwards, key="s")
my_canvas.onkey(fun=clear_sketch, key="c")



my_canvas.exitonclick()