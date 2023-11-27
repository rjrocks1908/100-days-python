import random
import tkinter as tk

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
WORDS_TO_LEARN_PATH = "data/words_to_learn.csv"
FRENCH_WORDS_PATH = "data/french_words.csv"

# ----------------- Generate Random words -----------------
try:
    df = pd.read_csv(WORDS_TO_LEARN_PATH)
except FileNotFoundError:
    df = pd.read_csv(FRENCH_WORDS_PATH)
french_words_with_translations = df.to_dict(orient="records")
word_map = {}


def add_to_csv(words_list):
    pd.DataFrame(words_list).to_csv(WORDS_TO_LEARN_PATH, index=False)


def flip_card():
    global word_map
    canvas.itemconfig(canvas_card_id, image=back_card_image)
    canvas.itemconfig(canvas_title_id, text="English", fill="white")
    canvas.itemconfig(canvas_word_id, text=word_map["English"], fill="white")


def display_french_word(button_id=0):
    global word_map, flip_timer_id
    window.after_cancel(id=flip_timer_id)
    word_map = random.choice(french_words_with_translations)
    canvas.itemconfig(canvas_card_id, image=front_card_image)
    canvas.itemconfig(canvas_title_id, text="French", fill="black")
    canvas.itemconfig(canvas_word_id, text=word_map["French"], fill="black")
    flip_timer_id = window.after(3000, func=flip_card)

    if button_id == 1:
        french_words_with_translations.remove(word_map)
        add_to_csv(french_words_with_translations)


# ----------------- UI -----------------
window = tk.Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer_id = window.after(3000, func=flip_card)

canvas = tk.Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)

# Card on Canvas
front_card_image = tk.PhotoImage(file="images/card_front.png")
back_card_image = tk.PhotoImage(file="images/card_back.png")
canvas_card_id = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(row=0, column=0, columnspan=2)

# Language Text on Canvas
canvas_title_id = canvas.create_text((400, 150), font=LANG_FONT, text="Title")
# Word Text on Canvas
canvas_word_id = canvas.create_text((400, 263), font=WORD_FONT, text="Word")

# wrong button
wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=lambda: display_french_word(0))
wrong_button.grid(row=1, column=0)

# right button
right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=lambda: display_french_word(1))
right_button.grid(row=1, column=1)

display_french_word()

window.mainloop()
