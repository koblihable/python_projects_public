from turtle import Screen
from cursor import Cursor
import random

SIZE = 50
SHAPE = "circle"
SPEED = "slowest"


color_list = [(0, 0, 0), (237, 230, 233), (201, 161, 92), (164, 65, 52), (157, 59, 73), (128, 162, 190), (212, 84, 56),
              (224, 206, 120), (65, 37, 55), (201, 136, 161), (58, 50, 104), (65, 82, 147)]

cursor = Cursor()
cursor.add_shape_size_speed(shape=SHAPE, size=SIZE, speed=SPEED)
cursor = cursor.get_cursor()
x_axis = -200
y_axis = -200
cursor.teleport(x_axis, y_axis)

screen = Screen()
screen.colormode(255)

for line in range(10):
    for dot in range(10):
        cursor.color(random.choice(color_list))
        cursor.stamp()
        cursor.penup()
        cursor.forward(50)
    y_axis += 50
    cursor.teleport(x_axis, y_axis)











screen.exitonclick()