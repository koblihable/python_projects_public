from turtle import Turtle

MOVE_SPEED = 20

class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.setx(x_pos)
        self.create_paddle()

    def create_paddle(self):
        self.shape("paddle")
        self.color("white")
        self.speed("fastest")
        self.penup()

    def move_up(self):
        self.sety(self.ycor() + MOVE_SPEED)

    def move_down(self):
        self.sety(self.ycor() - MOVE_SPEED)




