from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.l_pos = (-100, 200)
        self.r_pos = (100, 200)
        self.create_board(self.l_score, self.l_pos)
        self.create_board(self.r_score, self.r_pos)

    def create_board(self, score, position):
        self.goto(position)
        self.write(score, align="center", font=("Courier", 80, "normal"))

    def update_right_score(self):
        self.clear()
        self.r_score += 1
        self.create_board(self.r_score, self.r_pos)
        self.create_board(self.l_score, self.l_pos)

    def update_left_score(self):
        self.clear()
        self.l_score += 1
        self.create_board(self.l_score, self.l_pos)
        self.create_board(self.r_score, self.r_pos)
