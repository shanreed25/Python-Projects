from turtle import Turtle
COLOR = "white"
ALIGN = "center"
FONT_TYPE = "Arial"
FONT_SIZE = 25
FONT_STYLE = "normal"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(0, 265)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ", align=ALIGN, font=(FONT_TYPE, FONT_SIZE, FONT_STYLE))

    # Trigger when collision with wall or tail
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGN, font=(FONT_TYPE, FONT_SIZE, FONT_STYLE))

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



        #clear the writing when the score is updated