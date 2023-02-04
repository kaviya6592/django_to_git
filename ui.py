from tkinter import *
from quiz_b import Quiz
theme_color="#375362"


class Quizzler:
    def __init__(self,quiz_brain:Quiz):
        self.quiz=quiz_brain

        self.window = Tk()
        self.window.title("new")
        self.window.config(padx=20, pady=20, bg=theme_color)

        #self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.score_label = Label(text="score:0", fg="white",bg=theme_color)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150, 125,width=280, text="some question", fill=theme_color)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.true_button = Button(text="true", highlightthickness=0,command=self.true_press)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(text="false", highlightthickness=0,command=self.false_press)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
          self.canvas.config(bg="white")
          if self.quiz.still_has_question():
              self.score_label.config(text=f"score:{self.quiz.score}")
              q_text = self.quiz.next_question()
              self.canvas.itemconfig(self.question_text, text=q_text)
          else:
              self.canvas.itemconfig(self.question_text, text="you have reached end of quiz")
              self.true_button.config(state="disabled")
              self.false_button.config(state="disabled")




    def true_press(self):
          ques_answer= self.quiz.checkanswer("true")
          self.give_feedback(ques_answer)

          #self.canvas.itemconfig(self.score_label, text=f"score{ques_answer}")

    def false_press(self):
         ques_answer = self.quiz.checkanswer("false")
         self.give_feedback(ques_answer)
    #self.canvas.itemconfig(self.score_label, text=f"score{ques_answer}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question())
















