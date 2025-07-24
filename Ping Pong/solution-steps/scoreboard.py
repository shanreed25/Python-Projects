from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


# My Solution*****************************************************************************

# class ScoreBoard(Turtle):
#     def __init__(self, position):
#         self.position = position
#         self.score = 0
#         super().__init__()
#         self.hideturtle()
#         self.penup()
#         self.color("white")
#         self.goto(self.position)
#         self.pendown()
#         self.update_scoreboard()
#
#     def update_scoreboard(self):
#         self.write(f"Score: {self.score} ")
#
#     def score_point(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()