import html

class Quiz:
    def __init__(self,q_list):
        self.ques_no =0
        self.q_list1 =q_list
        self.score=0




    def still_has_question(self):
         return self.ques_no<len(self.q_list1)



    def next_question(self):
        self.current_question = self.q_list1[self.ques_no]
        #print(current_question)
        self.ques_no+=1
        q_text= html.unescape(self.current_question[0])
        return f"Q.{self.ques_no}{q_text}(true/false)"
        #current_qus_ans=current_question[1]
        #self.checkanswer(answer,current_qus_ans)


    def checkanswer(self,userans):

            correctans=self.current_question[1]
            if userans.lower()==correctans.lower():
                print("you are right")
                self.score += 1
                return self.score

            else:
                print("you are wrong")
                print(f"your answer is not right the correct answer is {correctans}")
                print(f"your current score is {self.score}/{self.ques_no}")













