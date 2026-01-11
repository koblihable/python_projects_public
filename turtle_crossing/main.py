from turtle import Screen
from cars import Cars
from player import Player
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=1000, height=500)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

score_board = ScoreBoard()
cars = Cars()

game_on = True

while game_on:

    time.sleep(0.1)
    screen.update()

    # move each car backward

    cars.create_car()
    cars.move()

    if player.is_at_top():
        player.go_to_bottom()
        score_board.increase_score()
        cars.speed_up()

    for car in cars.cars:
        if player.collision(car.position()):
            score_board.game_over()
            game_on = False








screen.exitonclick()