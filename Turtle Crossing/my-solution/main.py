import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard




screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

# TODO -1 Create Turtle Player
my_turtle = Player()
# TODO -2 Listen for the "Up" keypress to move the turtle north
screen.onkey(fun=my_turtle.move, key="Up")

# TODO-6 Create a scoreboard that keeps track of which level the user is on
level = Scoreboard()

game_is_on = True
loop_num = 0
cars = []
move_increment = 5
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_num += 1

    if loop_num % 6 == 0:# generate a new car only every 6th time the game loop runs
        # TODO-3 Create Cars
        new_car = CarManager()
        cars.append(new_car)

    for car in cars:
        car.move(move_increment) # move cars
        # TODO-4 Detect when the turtle player collides with a car
        if my_turtle.distance(car) < 30:
            level.game_over()# turtle hits a car, GAME OVER should be displayed in the center
            game_is_on = False# stop the game
            
    # TODO-5 Detect when the turtle player has reached the top edge of the screen(the FINISH_LINE_Y)
    if my_turtle.ycor() > 285:
        my_turtle.start_again()# reset game
        move_increment += 10 # make the cars go faster
        level.level_up()# increase the level when a player crosses successfully

screen.exitonclick()