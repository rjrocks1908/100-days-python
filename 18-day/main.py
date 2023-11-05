import colorgram
import turtle as t
import random

colors = colorgram.extract('image.jpg', number_of_colors=30)
colors_in_rgb = []
for color in colors:
    rgb = color.rgb
    colors_in_rgb.append((rgb.r, rgb.g, rgb.b))

t.colormode(255)
t.penup()
y = -250
x = -250
t.goto(x, y)
t.speed("fastest")
t.hideturtle()

for _ in range(10):
    t.penup()
    y = y + 50
    t.goto(x, y)
    for _ in range(10):
        t.pendown()
        t.dot(20, random.choice(colors_in_rgb))
        t.penup()
        t.forward(50)

t.exitonclick()
