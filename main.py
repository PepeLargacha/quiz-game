from data import question_data as data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(data)):
    question_bank.append(Question(data[i]['text'], data[i]['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.end_quiz()
