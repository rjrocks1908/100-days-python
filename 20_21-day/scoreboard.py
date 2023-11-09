from turtle import Turtle

ALIGNMENT = "center"
COLOR = "white"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.setposition(0, 280)
        self.update_scoreboard()

    def game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
