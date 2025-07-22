from turtle import Turtle, Screen
import time

my_canvas = Screen()
my_canvas.setup(width=600, height=600)
my_canvas.bgcolor("black")
my_canvas.title("Snake Game")
my_canvas.tracer(0)

#Create Snake Body
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("purple")
    new_segment.goto(position)
    segments.append(new_segment)

# this is causing the code below it not to work so we have to move it
# FIND OUT WHY LATER?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
# my_canvas.update()
# screen.update() might not execute as expected because screen.update() typically pauses the program
# to display the changes made to the turtle graphics window
# To ensure your code runs, you need to either call screen.mainloop() or turtle.done() at the end of your script,
# or strategically place screen.update() calls to avoid blocking the execution flow.




# Move Snake: Part - 1***********************************************************************************************************************************************************

#*********CODE START*********########################################################################################
# snake_is_moving = True
# while snake_is_moving:
#     for seg in segments:
#         seg.forward(20)
#         my_canvas.update()# updates the screen after each segment has moved
#         time.sleep(1)# used to slow down animation so we can see what happening
#*********CODE END*********########################################################################################

# the first segment will move, then the screen will update, sleep for 1 sec
# then the second segment will move, then the screen will update, sleep for 1 sec
# then the 3rd segment will move, then the screen will update, sleep for 1 sec
# then it will repeat
# so we need to move the my_canvas.update() outside of the for loop

# Move Snake: Part - 2***********************************************************************************************************************************************************

#*********CODE START*********######################################################################################
# snake_is_moving = True
# while snake_is_moving:
#     my_canvas.update()# updates the screen after each segment has moved
#     time.sleep(0.1)# slows the down animation so we can see what happening
#     for seg in segments:
#         seg.forward(20)
#         segments[0].left(90)
#*********CODE END*********########################################################################################
# so if we try to turn the snake head, the first segment will turn but, the second and third will keep moving forward
# this happens because the segments are not linked

# so instead of moving everything forwards, we can move the 3rd segment to move to the 2nd segment's position
# move the 2nd segment to the 1st segment position
# then get the first segment to make the move
# to do this we have to change the for loop

# Move Snake: Part - 3***********************************************************************************************************************************************************

#*********CODE START*********########################################################################################
# snake_is_moving = True
# while snake_is_moving:

# #range: where to start(start) where to stop(stop) how to get to move from start to stop(step)
#     # so if want a range of  1, 2, 3 it would be range(start=1, stop=3 step=1)
#     # if want a range of  3, 2, 1 it would be range(start=3, stop=1 step=-1)
#     # [(0, 0), (-20, 0), (-40, 0)], we want to start at index 2 and stop at 0 so its range(start=2, stop=0 step=-1)
#     # the range() function is not pure python, it comes from the C language, so it will not let us
#     # use the parameter names and we will get: TypeError: range() takes no keyword arguments
#     # for seg_num in range(2, 0, -1):
#     # hard coded start(2) removed so if the number of segments change then the code will still work
#     for seg_num in range(len(segments) - 1, 0, -1):
#         # MOVE THE 3RD SEGMENT TO THE POSITION OF THE 2ND SEGMENT************************************************
#         # when the loop starts, seg_num will be 2, which is the last segments position coordinates

#         # we need to get the 2nd segment's position so we can move the 3rd segment to that position
#         new_x = segments[seg_num -1].xcor() # 2nd segments x coordinate
#         new_y = segments[seg_num - 1].ycor()# 2nd segments y coordinate

#         segments[seg_num].goto(new_x, new_y)# the 3rd segment needs to go to the 2nd segment's coordinates
#     segments[0].forward(20)
#     segments[0].left(90)
#*********CODE END*********########################################################################################


# Move Snake: Final part***********************************************************************************************************************************************************

snake_is_moving = True
while snake_is_moving:
    my_canvas.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)

my_canvas.exitonclick()




