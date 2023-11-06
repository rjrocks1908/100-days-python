import random
import turtle as t

is_race_on = False
t.setup(width=500, height=400)
user_bet = t.textinput(title="Make your bet",
                       prompt="Which turtle will win the race?\n Choose among red, orange, yellow, green, blue and "
                              "purple,\n Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-120, -70, -20, 30, 80, 130]
turtles = []

for idx in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[idx])
    new_turtle.goto(x=-230, y=y_pos[idx])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

winner_color = None
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            is_race_on = False
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winner_color == user_bet:
    print(f"You win, {winner_color} wins the race!")
else:
    print(f"You lose, {winner_color} wins the race!")

t.exitonclick()
