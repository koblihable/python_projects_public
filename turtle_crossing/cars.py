from turtle import Turtle
import random

SPEED_UP = 5

#COLORS = [(65,105,225), (107,142,35), (225,215,0), (225,0,0), (199,21,133), (255,140,0)]
COLORS = ["royal blue", "olive drab", "gold", "red", "medium violet red", "dark orange"]

class Cars():

    def __init__(self):
        self.cars = []
        self.speed = 5

    def create_car(self):
        chance = random.randint(1, 10)
        if chance == 1:
            car = Turtle(shape="square")
            car.penup()
            car.resizemode("user")
            car.shapesize(stretch_len=2)
            car.goto(x=500, y=self.set_car_position())
            car.color(random.choice(COLORS))
            self.cars.append(car)

    @staticmethod
    def set_car_position():
        return random.randrange(-250, 250)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += SPEED_UP

