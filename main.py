from data import question_data
from question_model import Question
from quiz_brain import QuestionBrain
# loop through the data and create question objects from the data

question_bank = []


def questions_list():
    questions = []
    for question in question_data:
        questions.append(Question(question['text'], question["answer"]))
    return questions


question_bank = questions_list()

quiz = QuestionBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
