from turtle import Turtle

SHAPE = "square"
COLOR = "white"


class Paddle(Turtle):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.x = x
        self.y = y
        self.create_paddle()

    def create_paddle(self):
        self.goto(x=self.x, y=self.y)

    def up(self):
        new_y = self.ycor() + 20
        if new_y > 280:
            new_y = 280
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        if new_y < -280:
            new_y = -280
        self.goto(self.xcor(), new_y)
