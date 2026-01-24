import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.q_list = q_list
        self.score = 0
        self.current_question = None

    def still_have_questions(self):
        return self.question_number <= len(self.q_list)

    def next_question(self):
        self.current_question = self.q_list[self.question_number]
        self.question_number += 1
        text = html.unescape(self.current_question.text)
        return f"{self.question_number}: {text}"

    def check_answer(self, answer):
        if answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        else:
            return False


