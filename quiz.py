
class Quiz:
    def __init__(self, question: str, answers: list, true_answer: str):  # Кароче ВОПРос типа строка а ответы типа список ХЗ
        self.question = question
        self.answers = answers
        self.true_answer = true_answer

    def print_question(self):  # Это метод для того что бы вывести вопрос
        print(self.question)

    def print_answers(self):  # ну а тут Ответы
        for answer in self.answers:
            print(answer)
    def check_user_answer(self, user_answer):
        if user_answer.lower() == self.true_answer.lower():
            print("Правильный Ответ")


question1 = Quiz(question="Ты Руслан?", answers=["Да", "Нет"], true_answer="Да")


def first_logic():
    question1.print_question()
    question1.print_answers()
    user_answer = input("Твой Ответ: ")
    question1.check_user_answer(user_answer)
# хочу спать ваще
# не спи
