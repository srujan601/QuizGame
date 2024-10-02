
class QuizBrain:

    def __init__(self,question_list):
        self.question_nu=0;
        self.score=0;
        self.question_list=question_list;

    def still_has_question(self):
        return self.question_nu < len(self.question_list)

    def nextQuestion(self):
        current_question=self.question_list[self.question_nu];
        self.question_nu+=1;
        user_answer=input(f"Q {self.question_nu}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()== correct_answer.lower():
            self.score += 1;
        else:
            print("That's Wrong")
        print(f"Correct Answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_nu}")


