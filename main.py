from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import time

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

continue_game = True
while continue_game:
    test = quiz.next_question()
    # print(test)
    if not test:
        continue_game = False
        print(f"That was incorrect, {quiz.score} is your final score.")
    else:
        print("GoodJob, Next Question.\n")
        time.sleep(2)
        quiz.score += 1



