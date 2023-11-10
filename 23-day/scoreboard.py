from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto((-280, 250))
        self.curr_level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto((-200, 260))
        self.curr_level += 1
        self.write(f"Level: {self.curr_level}", align="center", font=FONT)

    def game_over(self, text):
        self.goto(0, 0)
        self.write(text, align="center", font=FONT)
