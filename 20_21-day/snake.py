import turtle as tt

SNAKE_SHAPE = "square"
SNAKE_COLOR = "white"
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head: tt.Turtle = self.segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            new_segment = tt.Turtle(shape=SNAKE_SHAPE)
            new_segment.penup()
            new_segment.color(SNAKE_COLOR)
            new_segment.width(width=20)
            new_segment.goto(x=x - i * 20, y=y)
            new_segment.heading()
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)
