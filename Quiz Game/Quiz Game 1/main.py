from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# a_question = Question(question_data[0]["text"], question_data[0]["answer"])
#
# print(a_question.text)

question_bank = []
# for i in question_data:
#     question_bank.append(Question(i["text"], i["answer"]))

for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
print(question_bank)


quiz = QuizBrain(question_bank)
# current_question = quiz.next_question()
# print(current_question)

while quiz.still_has_questions():
    quiz.next_question()

