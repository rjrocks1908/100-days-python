from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

TEXT = "text"
ANSWER = "answer"

question_bank = []

for data in question_data:
    question = data[TEXT]
    answer = data[ANSWER]
    question_bank.append(Question(text=question, answer=answer))

quiz = QuizBrain(q_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
