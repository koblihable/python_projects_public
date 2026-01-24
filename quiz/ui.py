import tkinter as tk
from tkinter import PhotoImage

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # display the score
        self.score_label = tk.Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, pady=20, padx=20)

        # display current question
        self.question_canvas = tk.Canvas(width=300, height= 250, bg="white")
        self.question_text = self.question_canvas.create_text(150,
                                                              125,
                                                              text="",
                                                              fill="black",
                                                              font=("Arial", 20, "italic"),
                                                              width=250)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # check the answer with input true
        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = tk.Button(image=self.right_image, highlightthickness=0, bg=THEME_COLOR, command=self.answer_correct)
        self.right_button.grid(column=0,row=2, pady=20, padx=20)

        # check the answer with input right
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = tk.Button(image=self.wrong_image, highlightthickness=0, bg=THEME_COLOR, command=self.answer_wrong)
        self.wrong_button.grid(column=1, row=2, pady=20, padx=20)

        self.display_question()

        self.window.mainloop()

    def display_question(self):
        self.question_canvas.config(bg="white")
        if self.quiz.still_have_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="The end")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def answer_correct(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def answer_wrong(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg="green")
        else:
            self.question_canvas.config(bg="red")
        self.window.after(1000, self.display_question)
