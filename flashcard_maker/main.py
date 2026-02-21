import tkinter as tk
from tkinter import PhotoImage
import pandas
import random
import json

BACKGROUND_COLOR = "#B1DDC6"

### data ###

vocab_df = pandas.read_csv("data/finnish.csv")
vocab_dictionary = vocab_df.to_dict(orient="records")
word = {}


### card functionality ###

def pick_word():

    global word
    global vocab_dictionary

    file = "words_to_learn.json"
    try:
        with open("words_to_learn.json", "r", encoding='utf-8') as f:
            data = json.load(f)

    except FileNotFoundError:
        word = random.choice(vocab_dictionary[:10])
        with open("words_to_learn.json", "w", encoding='utf-8') as f:
            json.dump(vocab_dictionary[:10], f, indent=4)

    else:
        try:
            word = random.choice(data)
            data.remove(word)
            with open("words_to_learn.json", "w", encoding='utf-8') as f:
                json.dump(data, f, indent=4)

        except IndexError:
            pass

    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(vocab, text=word["english"], fill="black")
    canvas.itemconfig(language, text="English", fill="black")


def flip_card():

    canvas.itemconfig(canvas_image, image=reverse_image)
    canvas.itemconfig(vocab, text=word["finnish"], fill="white")
    canvas.itemconfig(language, text="Finnish", fill="white")
    window.after(3000, func=pick_word)

### UI setup ####

window = tk.Tk()
window.title("Flashy")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="images/card_front.png")
reverse_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
language = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
vocab = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 40, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
pick_word()

right_image = PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command=pick_word)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image, highlightthickness=0, command=flip_card)
wrong_button.grid(column=0, row=1)




window.mainloop()