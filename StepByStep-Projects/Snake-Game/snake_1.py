from turtle import Turtle
# these constant are used in case we wanted to change the values
# like if we want to start at different position or to move further
# we won't have to look through the code to change any of the values, we can just change it here
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # head of snake

    # def create_snake(self):
    #     for position in STARTING_POSITIONS:
    #         new_segment = Turtle("square")
    #         new_segment.penup()
    #         new_segment.color("purple")
    #         new_segment.goto(position)
    #         self.segments.append(new_segment)


    # create_snake and add_segment creates the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("purple")
        new_segment.goto(position)
        self.segments.append(new_segment)


    # Grow snake
    def grow(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

# Move Snake Up, Down, Left Right:

    # Add a condition to ensure the snake doesn't immediately reverse its direction.
    # For instance, if the snake is currently moving down (heading 270),
    # it should not be allowed to instantly turn up
    def move_up(self):
        #prevent the snake from immediately reversing direction
        if self.head.heading() != DOWN: # Prevent reverse movement: Prevent moving directly up from down
            #use the setheading() method of your snake's head
            # to set its direction to 90 degrees(north)
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:  # Prevent moving directly down from up
        # use the setheading() method of your snake's head
        # to set its direction to 270 degrees(south)
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT: # Prevent moving directly left from right
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT: # Prevent moving directly right from left
            self.head.setheading(RIGHT)



#**************************************************

##self.tail = self.segments[len(self.segments) - 1]
 # # Grow snake
 #    def grow(self):
 #        new_segment = Turtle("square")
 #        new_segment.penup()
 #        new_segment.color("purple")
 #        self.segments.append(new_segment)
























































#SOLUTION -2*******************************************************************************************************
# class SnakeBody:
#     def __init__(self):
#         self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
#         self.segments = []
#         for position in self.starting_position:
#             new_segment = Turtle("square")
#             new_segment.penup()
#             new_segment.color("purple")
#             new_segment.goto(position)
#             self.segments.append(new_segment)
#
#
# class Snake:
#     def __init__(self):
#         self.body = SnakeBody()
#     def move(self):
#         for seg_num in range(len(self.body.segments) - 1, 0, -1):
#             new_x = self.body.segments[seg_num - 1].xcor()
#             new_y = self.body.segments[seg_num - 1].ycor()
#             self.body.segments[seg_num].goto(new_x, new_y)
#         self.body.segments[0].forward(20)
#         self.body.segments[0].left(90)