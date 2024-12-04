# Словарь с вопросами и ответами, первый слот ответа хранит индекс правильного ответа
questions = {
    "Ты руслан?": [0, "Да", "Нет"],
    "мяу мяу?": [1, "гав", "мяу"],
    #"Вопрос": [true_index, "Ответы",.....]
}


def get_answer_from_user():
    #  Возвращает введенный индекс от пользователя, надо ту реализовать Ошибки ввода
    return int(input("Введите ответ: "))


class Question:
    # класс ВОПРОС как экземпляр в себе будет хранить вопросы ответы и правильный индекс ответа
    def __init__(self, question, answers, true_answer):
        self.question = question  # Хранит вопрос
        self.answers = answers  # Хранит ответ
        self.true_answer = true_answer  # хранит типа индекс правильного ответа

    def check_answer(self):
        # Простая проверка ответа
        if get_answer_from_user() == self.true_answer:
            print("Правильно")
        else:
            print("Неправильно")


class Quiz:
    # Класс квиз в котором будут всякие генераторы и обработка вопросов
    def __init__(self):
        self.questions = []

    def get_questions_from(self, questions_file):
        # Создает экземпляры вопросов
        for quest, answer in questions_file.items():
            make_quest = Question(question=quest, answers=answer[1:], true_answer=answer[0])
            self.questions.append(make_quest)


class GUI:
    # Простой класс Графики, че ваще подумал я ботов изучаю и совершенствую
    # как работать с Аиограмм По сути в ТГ можно сделать графику потом как-нибудь
    def __init__(self, quiz):
        self.quiz = quiz
        pass

    def print_questions(self):
        index_of_quest = 1
        for quest in self.quiz.questions:
            index_of_answer = 0

            print(f"Вопрос номер: {index_of_quest}")
            print(quest.question)
            for answer in quest.answers:
                print(index_of_answer, answer)
                index_of_answer += 1
            quest.check_answer()
            index_of_quest += 1


quiz = Quiz()  # САСдаем экземпляк клсса Квиз
gui = GUI(quiz)  # Экземпляр графики


def first_logic():
    quiz.get_questions_from(questions_file=questions)  # Получаем вопросы
    gui.print_questions()  # Рисуем вопросы


# хочу спать ваще
# не спи
# не сплю