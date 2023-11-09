import turtle as tt
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

tt.setup(width=800, height=600)
tt.bgcolor("black")
tt.title("Pong Game")
tt.tracer(0)
tt.listen()

l_paddle = Paddle(x=350, y=0)
r_paddle = Paddle(x=-350, y=0)
tt.onkeypress(key="Up", fun=l_paddle.up)
tt.onkeypress(key="Down", fun=l_paddle.down)
tt.onkeypress(key="w", fun=r_paddle.up)
tt.onkeypress(key="s", fun=r_paddle.down)

ball = Ball()
scoreboard = Scoreboard()

is_game_on = True
while is_game_on:
    tt.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(l_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_right_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_left_score()

tt.exitonclick()
