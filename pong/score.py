from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,430)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{self.left_score} : {self.right_score}", move=False, align="center", font=('Arial', 12, 'normal'))

    def increase_left_score(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_right_score(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", move=False, align="center", font=('Arial', 14, 'normal'))