from turtle import Turtle
import random
from typing import List

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars: List[Turtle] = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(x=330, y=random.randint(-250, 250))
        self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increment_speed(self):
        self.move_speed += MOVE_INCREMENT

    def pop_first(self):
        self.all_cars.pop(0)

    def is_collision(self, turtle: Turtle):
        for car in self.all_cars:
            if car.distance(turtle) < 20:
                return True
