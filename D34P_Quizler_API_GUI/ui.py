from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#F0E161"
OTHER_COLOR = "#2B4865"
RED= "#D61C4E"
GREEN = "#59CE8F"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QuiZZler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg=OTHER_COLOR, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.que_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"))

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(width=75, height=75, image=wrong_img, bg=THEME_COLOR, command=self.press_wrong)
        self.wrong_button.grid(column=0, row=3)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(width=75, height=75, image=right_img, bg=THEME_COLOR, command=self.press_right)
        self.right_button.grid(column=1, row=3)

        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Impact", 20, "bold"), bg=THEME_COLOR, fg=OTHER_COLOR)
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.get_next_que()

        self.window.mainloop()

    def get_next_que(self):
        self.canvas.config(bg=OTHER_COLOR)
        if self.quiz.still_has_questions():
            que_text = self.quiz.next_question()
            self.canvas.itemconfig(self.que_text, text=que_text)

        else:
            self.wrong_button.config(state="disabled")
            self.right_button.config(state="disabled")

            self.canvas.itemconfig(self.que_text,
                                   text=f"QUIZ Completed\nYour Score {self.quiz.score}/{self.quiz.question_number} ")

    def press_wrong(self):
        user_answer = "False"
        self.check_ans(user_answer)

    def press_right(self):
        user_answer = "True"
        self.check_ans(user_answer)

    def check_ans(self, user_answer):
        if self.quiz.check_answer(user_answer):
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)

        self.score_label.config(text=f"Score: {self.quiz.score}")

        self.window.after(100, self.get_next_que)

