class QuizBrain:
    def __init__(self,qlist):
        self.qlist=qlist
        self.qnum=0
        self.score=0

    def still_q(self):
        return self.qnum < len(self.qlist)


    def next_q(self):
        current_question=self.qlist[self.qnum]
        self.qnum +=1
        uans=input(f"Q.{self.qnum} {current_question.qtext} (True/False): ")
        self.check_ans(uans, current_question.qans)
    
    def check_ans(self, uans, correct_answer):
        if uans.lower() == correct_answer.lower():
            print("you got it right!")
            self.score+=1
        else:
            print("Thats wrong.")
        print(f"The correct was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.qnum}")
        print("\n")