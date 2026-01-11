from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_bottom()
        self.speed("fastest")

    def move_up(self):
        self.forward(10)

    def go_to_bottom(self):
        self.goto(x=0, y=-260)

    def is_at_top(self):
        return self.ycor() > 250

    def collision(self, position):
        return self.distance(position) < 5