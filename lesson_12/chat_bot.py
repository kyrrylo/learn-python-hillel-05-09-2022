# из модуля random импортировать метод choice (выбирает случайное значение из списка)
from random import choice
import json
import os


class ChatBot:
    def __init__(self, name: str, vocab: dict):
        self.name = name
        self.vocab = vocab

    def save(self):
        filename = f'{self.name}.json'
        json.dump(self.vocab, open(filename, 'w'))
        print(f'Chatbot data was successfully saved to {filename}')

    def load(self):
        filename = f'{self.name}.json'
        if os.path.isfile(filename):
            self.vocab = json.load(open(filename))
            print(f'Chatbot data was successfully loaded from {filename}')
        else:
            print(f'Could not find file to load from: {filename}, using default data')

    def have_a_conversation(self):
        """
        Считывает ответы пользователя, передаёт их на обработку,
        пока не будет пора выходить
        """
        while True:
            user_input = self.get_user_message()
            exit_flag = self.respond(message=user_input.lower())
            if exit_flag:
                break

    def print_bot_message(self, reponse: str):
        print(f'{self.name}: {reponse}')

    def get_user_message(self):
        user_input = input('You: ')
        return user_input

    def learn_from_user(self, message: str):
        """
        Выбирать случайное слово из сообщения пользователя и спрашивать что оно означает
        Ответ будет записан в базу знаний нашего бота
        Так же функция будет благодарить пользователя за науку)
        :param message: ввод пользователя, переведённый в нижний регистр,
        в котором не найдено знакомых ключевых слов
        """
        new_keyword = choice(message.split())
        self.print_bot_message(f'Що ви маєте на увазі кажучи: {new_keyword}?')
        user_input = input('You: ')
        self.vocab[new_keyword] = ([user_input], False)
        self.print_bot_message(f'Дякую, зрозумів!')

    def respond(self, message: str) -> bool:
        """
        Найти ответ на ввод пользователя
        :param message: ввод пользователя, переведённый в нижний регистр
        :return: флажок пора ли выходить (да - пора, нет - не пора)
        """
        # поиск по известным боту ключевым словам
        for key, (response_options, exit_flag) in self.vocab.items():
            if key in message:
                self.print_bot_message(choice(response_options))
                return exit_flag
        # что происходит если ни одно ключевое слово не подошло
        self.learn_from_user(message)
        # возвращаем отрицательный флаг выхода (не выходим)
        return False


if __name__ == '__main__':
    # vocab structure
    # key - ключевое слово от пользователя
    # value - кортёж из двух элементов
    # первый элемент - список возможных ответов чатбота
    # второй элемент - флажок пора ли выходить
    chatbot = ChatBot(name='Neil', vocab={
        "привіт": (["Доброго вечора, я бот з України!", "Привііііт!"], False),
        "доброго дня": (["Доброго вечора, я бот з України!", "Привііііт!"], False),
        "хай": (["Доброго вечора, я бот з України!", "Привііііт!"], False),
        "бувай": (["Побачимось у мережі", "Бувай)"], True),
        "надобраніч": (["Побачимось у мережі", "Бувай)"], True),
        "гудбай": (["Побачимось у мережі", "Бувай)"], True),
        "до зустрічі": (["Побачимось у мережі", "Бувай)"], True)
    })
    chatbot.load()
    chatbot.have_a_conversation()
    chatbot.save()

# наследование
# инкапсуляция
# полиморфизм
