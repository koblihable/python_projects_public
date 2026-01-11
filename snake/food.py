from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.move_food()

    @staticmethod
    def set_coordinates():
        x = random.randint(-440, 440)
        y = random.randint(-440, 440)
        return x,y

    def move_food(self):
        self.goto(self.set_coordinates())







