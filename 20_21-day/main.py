import turtle as tt
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

tt.setup(width=600, height=600)
tt.bgcolor("black")
tt.title("Snake Game")
tt.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

tt.listen()
tt.onkey(key="Up", fun=snake.up)
tt.onkey(key="Down", fun=snake.down)
tt.onkey(key="Left", fun=snake.left)
tt.onkey(key="Right", fun=snake.right)

is_game_over = False
while not is_game_over:
    tt.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_scoreboard()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_over = True

    # Detect collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_over = True

tt.exitonclick()
