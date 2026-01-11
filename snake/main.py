from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=1000,height=1000)
screen.screensize(900,900)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    if snake.head.distance(food) <= 15:
        food.move_food()
        snake.extend()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 450 or snake.head.xcor() < -450 or snake.head.ycor() > 450 or snake.head.ycor() < -450:
        scoreboard.game_reset()
        snake.snake_reset()

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) <= 10:
            scoreboard.game_reset()
            snake.snake_reset()




screen.exitonclick()