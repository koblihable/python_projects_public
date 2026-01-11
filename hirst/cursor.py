from turtle import Turtle
import random


class Cursor:
    def __init__(self):
        self.turtle = Turtle()

    @staticmethod
    def select_colour():
        r = round(random.random(), 3)
        g = round(random.random(), 3)
        b = round(random.random(), 3)
        return r, g, b

    # TODO remove?
    def get_cursor(self):
        return self.turtle

    def add_shape_size_speed(self, shape="arrow", size=5, speed="normal"):
        self.turtle.shape(shape)
        self.turtle.speed(speed)
        self.turtle.pensize(size)

    def add_random_colour(self):
        r, g, b = self.select_colour()
        self.turtle.color(r, g, b)
        return self.turtle