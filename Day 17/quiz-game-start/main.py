from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def create_bank(question_data):
    question_list = []
    for x in question_data:
        ## for normal data
        # new_question = Question(x['text'], x['answer'])
        # for data from opentdb.com
        new_question = Question(x['question'], x['correct_answer'])
        question_list.append(new_question)
    return question_list


question_bank = create_bank(question_data)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
