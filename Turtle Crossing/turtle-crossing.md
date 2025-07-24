# Step 1 - Check out how the game play works
1. A turtle moves forwards when you press the "Up" key
   - It can only move forwards, not back, left or right
2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge
3. When the turtle hits the top edge of the screen(finish line)
   - it moves back to the original position and the player levels up
   - On the next level, the car speed increases
4. When the turtle collides with a car, it's game over and everything stops.

# Step 2 - Break down the Problem
**The first step of creating any large project is to breakdown the problem into smaller, bite-sized chunks.
Add the following comments to the starting code and try to tackle them one-by-one.**

1. Create a turtle player that starts at the bottom of the screen
2. listen for the "Up" keypress to move the turtle north
3. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
    - move to the left edge of the screen
    - No cars should be generated in the top and bottom 50px of the screen
    - generate a new car only every 6th time the game loop runs
4. Detect when the turtle player collides with a car
   - stop the game if this happens
5. Detect when the turtle player has reached the top edge of the screen(the FINISH_LINE_Y)
   - return the turtle to the starting position
   - increase the speed of the cars
   - Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed
6. Create a scoreboard that keeps track of which level the user is on
   - Every time the turtle player does a successful crossing, the level should increase
   - When the turtle hits a car, GAME OVER should be displayed in the center