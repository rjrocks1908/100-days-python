import turtle as tt

import pandas as pd

ALIGNMENT = "center"
FONT = ("Arial", 8, "normal")

tt.title("U.S States Game")
image = "blank_states_img.gif"
tt.addshape(image)
tt.shape(image)
tt.penup()

data_states = pd.read_csv("50_states.csv")
state_names = data_states["state"].tolist()
correct_guesses = []

turtle_names = tt.Turtle()
turtle_names.penup()
turtle_names.hideturtle()

missing_states = []


def get_missed_states():
    for state in state_names:
        if state not in correct_guesses:
            missing_states.append(state)

    new_data = pd.Series(missing_states)
    new_data.to_csv("states_to_learn.csv")


while len(correct_guesses) < len(state_names):
    answer_state = tt.textinput(title=f"{len(correct_guesses)}/{len(state_names)} States Correct",
                                prompt="What's another state's name?").title()
    if answer_state == "Exit":
        get_missed_states()
        break

    if answer_state in state_names and answer_state not in correct_guesses:
        state_row = data_states[data_states["state"] == answer_state]
        turtle_names.setposition(x=int(state_row.x), y=int(state_row.y))
        turtle_names.write(arg=answer_state, align=ALIGNMENT, font=FONT)
        correct_guesses.append(answer_state)
