from turtle import Turtle, Screen
my_canvas = Screen()
my_canvas.setup(width=600, height=600)
my_canvas.bgcolor("black")
my_canvas.title("Snake Game")

# Create Snake Body: Part - 1*****************************************************************************************************
# Create Snake Body
# When the snake body is created, each segment appears on the screen at position (0, 0)
# the second segment needs to move to position (-20, 0) and the 3rd segment needs to move to position (-40, 0)
# this animation happens fast but, can be seen on the screen
# you can see this on the screen and we do not want this
# so we need to use screen.tracer(), screen.update

#*********CODE START*********######################################################################################
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.penup()
#     new_segment.color("purple")
#     new_segment.goto(position)
#     segments.append(new_segment)
#     time.sleep(2)# used to slow down animation just so we can see it in slow motion
#*********CODE End*********######################################################################################




#Create Snake Body: Part - 2**********************************************************************************************************
# Create Snake Body
# if we want to stop the animation(seen it part 1), we can use screen.tracer(0) to control the animation
# it takes a number as input and turns the animation off
# 0 turns it off

#*********CODE START*********######################################################################################
# my_canvas.tracer(0)# you must call screen.update() when you want the content to appear on the screen
# starting_position = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.penup()
#     new_segment.color("purple")
#     new_segment.goto(position)
#     segments.append(new_segment)


# #calling screen.update() here after all the segments have been created
# # so we do not see the animation of the segments being moved
# my_canvas.update()
#*********CODE END*********######################################################################################

#Create Snake Body: Final Code*****************************************************************************************************
my_canvas.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("purple")
    new_segment.goto(position)
    segments.append(new_segment)

my_canvas.update()



my_canvas.exitonclick()

