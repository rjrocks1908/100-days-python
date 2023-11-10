import turtle as tt
import time
import random
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

tt.setup(width=600, height=600)
tt.title("Turtle Crossing")
tt.tracer(0)

player = Player()
tt.listen()
tt.onkeypress(fun=player.go_up, key="w")

car_manager = CarManager()
scoreboard = Scoreboard()


def game():
    game_is_on = True
    num = 6
    while game_is_on:
        time.sleep(0.1)
        tt.update()

        # Generating Cars at random position
        if random.randint(1, num) == 1:
            car_manager.create_car()
        car_manager.move()

        # Pop cars from List once they disappear from screen
        cars_len = len(car_manager.all_cars)
        if cars_len != 0 and car_manager.all_cars[0].xcor() < -330:
            car_manager.all_cars.pop(0)

        # Collision with cars
        if car_manager.is_collision(player):
            scoreboard.game_over("Game Over")
            game_is_on = False

        # Resets the turtle position once it completes the level
        if player.ycor() > FINISH_LINE_Y:
            player.refresh()
            scoreboard.update_level()
            car_manager.increment_speed()
            if scoreboard.curr_level % 2 == 0:
                num -= 1
            if scoreboard.curr_level == 10:
                break

    if game_is_on:
        scoreboard.game_over("You Won")


if __name__ == '__main__':
    game()

tt.exitonclick()
