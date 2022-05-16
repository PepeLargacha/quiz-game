class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def game(self):
        while self.question_number != 10:
            current_question = self.question_number
            current_question_text = self.question_list[current_question].text
            current_question_answer = bool(self.question_list[current_question].answer)
            print(f"Q{current_question + 1}: {current_question_text}")
            user_answer = input('(True" or "False": )').lower()
            if user_answer == "true":
                user_answer = True
            else:
                user_answer = False

            if user_answer == current_question_answer:
                self.score +=1
                print("You got it right!")
                print(f"The correct answer was: {current_question_answer}")
                print(f"Your current score is: {self.score}/{current_question + 1}")
            else:
                print("That's wrong.")
                print(f"The correct answer was: {current_question_answer}")
                print(f"Your current score is: {self.score}/{current_question + 1}")
            self.question_number += 1
