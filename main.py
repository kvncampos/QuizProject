from question_model import Question
from data import question_data, json_list
from quiz_brain import QuizBrain

open_trivia_bank = []
question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

for key in json_list:
    q_text = key["question"]
    q_answer = key["correct_answer"]
    new_question = Question(q_text, q_answer)
    open_trivia_bank.append(new_question)


quiz = QuizBrain(open_trivia_bank)

while quiz.still_has_question():
    continue








