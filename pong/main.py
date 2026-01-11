from turtle import Screen
from pong_screen import ScreenDivider
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1400

RIGHT_SIDE = SCREEN_WIDTH / 2
LEFT_SIDE = -abs(RIGHT_SIDE)

# settings for the screen divider
###
#Y_SCREEN_TOP = SCREEN_HEIGHT / 2
#Y_SCREEN_BOTTOM = -abs(Y_SCREEN_TOP)
#Y_DIV_POSITIONS = []
#i = Y_SCREEN_TOP
#while i > Y_SCREEN_BOTTOM:
#    Y_DIV_POSITIONS.append(i)
#    i -= 120
###

# define shapes for the divider and the paddles
#divider = ((-30, 5), (30, 5), (30, -5), (-30, -5))
paddle = ((-50, 10), (50, 10), (50, -10), (-50, -10))

# define screen
screen = Screen()
screen.setup(width=1500, height=1000)
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer()

# register shapes
#screen.register_shape('divider', divider)
screen.register_shape('paddle', paddle)

# create the divider and the paddles
#div = ScreenDivider(Y_DIV_POSITIONS)
right_paddle = Paddle(RIGHT_SIDE)
left_paddle = Paddle(LEFT_SIDE)

# move paddles
screen.listen()
screen.onkey(right_paddle.move_up, key="Up")
screen.onkey(right_paddle.move_down, key="Down")
screen.onkey(left_paddle.move_up, key="w")
screen.onkey(left_paddle.move_down, key="s")

# create ball
ball = Ball()

#setup score board
score_board = ScoreBoard()

game_on = True
while game_on:
    ball.move()
    time.sleep(0.1)
    screen.update()

    if ball.should_bounce():
        ball.bounce()

    if ball.should_hit_paddle(right_paddle.pos()) or ball.should_hit_paddle(left_paddle.pos()):
        ball.hit_paddle()

    if ball.xcor() > 700 or ball.xcor() < -700:

        if ball.direction == "right":
            ball.reset_self()
            score_board.increase_left_score()
        elif ball.direction == "left":
            ball.reset_self()
            score_board.increase_right_score()

    if score_board.left_score == 10 or score_board.right_score == 10:
        score_board.game_over()
        game_on = False


screen.exitonclick()

