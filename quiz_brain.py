import os
import pdb
import time


class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.current_score = 0
        self.total_score = 0

    def reset(self):
        dic = vars(self)
        no_edit = ['q_list']
        for i in dic.keys():
            if i not in no_edit:
                dic[i] = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def still_has_question(self):

        game_continues = True
        while game_continues:
            try:
                test = self.next_question()
                # print(test)
                answer = self.q_list[self.q_number - 1].answer

                if not test:
                    print(f"Incorrect!\nThe answer was: {answer}")
                    time.sleep(1)
                    self.total_score += 1
                    print(f"Your current score is: {self.current_score}/{self.total_score}\n")

                else:
                    print(f"Correct!\nThe answer was: {answer}")
                    time.sleep(1)
                    self.current_score += 1
                    self.total_score += 1
                    print(f"Your current score is: {self.current_score}/{self.total_score}\n")
                    time.sleep(2)
            except IndexError:
                print(f"The Quiz is Complete.\nYour final score was: {self.current_score}/{self.total_score}")
                game_continues = False
        retry = input(f"Want to retry this quiz (Yes/No)? ").lower()
        if retry == "yes":
            print()
            self.reset()
            self.clear_screen()
            time.sleep(2)
            return True
        else:
            print("\nThank you for playing my Quiz Project Game. Goodbye.")
            time.sleep(2)
            return False

    def next_question(self):
        self.q_number += 1
        number = self.q_number
        question = self.q_list[self.q_number - 1]
        user_answer = input(f"Q{number}: {question.text} (True/False)? ").title()
        if user_answer == question.answer:
            return True
        else:
            return False
