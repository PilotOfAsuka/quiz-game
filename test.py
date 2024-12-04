
questions = {
    "Ты руслан?": ["Да", "Нет"]
}

def get_question():
    for quest, answer in questions.items():
        print(quest)
        print(answer)
    pass

get_question()