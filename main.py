from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for i in question_data:
    a=i["text"]
    b=i["answer"]
    new_q=Question(a,b)
    question_bank.append(new_q)
quiz=QuizBrain(question_bank)
while quiz.still_q():
    quiz.next_q()
print("You have completed the quiz.")
print(f"Your current score is: {quiz.score}/{quiz.qnum}")

