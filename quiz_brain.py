class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        self.q_number += 1
        number = self.q_number
        question = self.q_list[self.q_number - 1]
        user_answer = input(f"Q{number}: {question.text} (True/False) ").title()
        if user_answer == question.answer:
            return True
        else:
            return False
