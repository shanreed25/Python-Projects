class QuizBrain:
    def __init__(self, questions_list):
        self.question_list = questions_list
        self.question_number = 0
        self.score = 0

    # TODO-1 ask question
    # get the item at the current question_number from the question_list
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False) ")
        self.check_answer(user_answer, current_question.answer)

    # TODO-3 check if we are at the end of quiz
    def still_has_questions(self):
        # return self.question_number < len(self.question_list)
        #     or
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f"Quiz Complete")
            print(f"Your final score is: {self.score}/{self.question_number}")
            return False

    # TODO-2 check if the answer is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!!")
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")







