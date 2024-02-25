"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {}

def ask_user(answers_dict):
    repeat = "y"
    while repeat.lower() == "y":
        answer = input("Пользователь: ").capitalize()
        answer_bot = answers_dict.pop(answer, "Ответа нет")
        print(f"Программа: {answer_bot}")
        repeat = input("Хотите здать ворос еще раз? " +
                       "Введите y/да, n/нет.")

if __name__ == "__main__":
    ask_user(questions_and_answers)
