from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, position):
        self.position = position
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(self.position)
        self.pendown()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} ")

    def score_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
