from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
# new_qb = [Question(item["text"], item["answer"]) for question in question_data]
# print(question_bank[0].text)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("you completed you game")
print(f"Your final score is {quiz.score}/{quiz.question_no}")
