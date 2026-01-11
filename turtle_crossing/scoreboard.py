from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-450,200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.score}", move=False, align="center", font=('Arial', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 14, 'normal'))
