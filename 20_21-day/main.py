import turtle as tt
import time
from snake import Snake
from food import Food

tt.setup(width=600, height=600)
tt.bgcolor("black")
tt.title("Snake Game")
tt.tracer(0)

snake = Snake()
food = Food()

tt.listen()
tt.onkey(key="Up", fun=snake.up)
tt.onkey(key="Down", fun=snake.down)
tt.onkey(key="Left", fun=snake.left)
tt.onkey(key="Right", fun=snake.right)

while True:
    tt.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()

tt.exitonclick()
