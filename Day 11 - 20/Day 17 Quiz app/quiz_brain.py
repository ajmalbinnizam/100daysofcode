class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f"{self.question_no}. {current_question.text} (True/False)?: ")
        # if answer == current_question.answer:
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user_answer, current_answer):
        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("That was the wrong answer")
        print(f"The correct answer was: {current_answer}")
        print(f"Current score {self.score}/{self.question_no}")
        print("\n")

    def still_has_questions(self):
        return True if self.question_no < len(self.question_list) else False
