from question_model import Question
from data import question_data
from quiz_b import Quiz
from ui import Quizzler









question_bank = []

for question in question_data:
    question1=question["question"]
    answer1=question["correct_answer"]
    new_question =(question1,answer1)

    question_bank.append(new_question)
   # print(question_bank)

quiz = Quiz(question_bank)
quiz_ui= Quizzler(quiz)


#while quiz.still_has_question:
    #quiz.next_question()


print("u have coompleted the quiz")
print(f"ur final score{quiz.score}/{quiz.ques_no}")
