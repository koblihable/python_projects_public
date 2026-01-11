from turtle import Turtle
import random

HEADING = random.randrange(359)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.setup_ball()
        self.direction = self.get_direction()
        self.angle = None

    def setup_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.set_heading()

    def move(self):
        self.forward(20)
        self.get_direction()

    def set_heading(self):
        heading = random.randrange(359)
        while heading == 90 or self.heading == 270:
            heading = random.randrange(359)
        self.setheading(heading)

    def get_direction(self):
        if self.heading() < 90 or self.heading() > 270:
            self.direction = "right"
        else:
            self.direction = "left"
        return self.direction

    def should_hit_paddle(self, paddle_xcor):
        return self.distance(paddle_xcor) < 50 and (
                self.xcor() >= 680 or self.xcor() <= -680
        )

    def should_bounce(self):
        return self.ycor() >= 450 or self.ycor() <= -450

    def bounce(self):
         self.setheading((360 - self.heading()))

    def get_angle(self):
        return abs(180 - self.heading())

    def hit_paddle(self):
        if self.heading() < 180:
            self.setheading(self.get_angle())
        elif self.heading() < 360:
            self.setheading(360 - self.get_angle())

    def should_reset(self, paddle_xcor):
        return not self.should_hit_paddle(paddle_xcor) and (self.xcor() >= 680 or self.xcor() <= -680)

    def reset_self(self):
        self.reset()
        self.setup_ball()



