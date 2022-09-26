from time import time


def is_dict_empty(dict_to_test):
    if dict_to_test:
        print(f'{dict_to_test} - не пустой словарь')
    else:
        print(f'{dict_to_test} = пустой словарь')


def run_experiment(what_to_search: list, searchable_struct):
    t0 = time()
    for element in what_to_search:
        if element in searchable_struct:
            pass
            # print(f'yes, {element} is in {len(searchable_struct)} {type(searchable_struct)}')
        else:
            pass
            # print(f'no, {element} is not in {len(searchable_struct)} {type(searchable_struct)}')
    print(f'Searching in {type(searchable_struct)} {len(searchable_struct)} took {round(time() - t0, 3)}s')


if __name__ == '__main__':
    x = dict()  # это пустой словарь
    print(x, type(x))
    is_dict_empty(x)

    # Dictionary - словарь
    # {
    #   key1: value,
    #   key2: value,
    #   ...
    # }
    # ключом может быть только то, что хэшируется (ошибка будет unhashable если вы попробуете сделать ключом то, что не хэшируется)
    # ключом (key) в словаре не может быть список или другой словарь или любое другое множественное значение
    # key - клавиша или ключ
    # hashable - то, что можно привести к уникальному значению и сравнивать с другими ключами (хэшами) в этом словаре
    x = {
        "key": 'ключ',
        "key": 'клавиша',  # эти значения перетрутся, останется только более позднее
        'first name': 'Andrey',
        'last name': 'Andreiev',
        'age': 25,
        '0': 6,  # а вот так можно, потому что разные типы данных
        0: 5,
        0.0: 7,  # а вот числовые перетирают друг друга
        is_dict_empty: [5, 6, 7]
    }

    is_dict_empty(x)

    # операция поиска
    if 'a' in 'ababagalamaga':
        print('yes')
    # Эксперимент где быстрее искать - в словаре или в списке
    len_to_test = 10000
    elements_to_search = [-50, 50, 100, -20, 10000, 990, 452, 12304] * 1000
    t0 = time()
    # list comprehension
    thousand_list = [i for i in range(len_to_test)]
    # dictionary comprehension
    thousand_dict = {i: i for i in range(len_to_test)}
    print(f'Generating data took {round(time() - t0, 2)}s')

    run_experiment(elements_to_search, thousand_dict)
    run_experiment(elements_to_search, thousand_list)

    # how to declare a dictionary
    x = {
        'first name': 'Andrey',
        'last name': 'Andreiev',
        'age': 25
    }
    print(x)
    # как параметры функции
    d = dict(first_name='Andrey', last_name='Andreiev', age=25)
    print(d)
    # списком котртежей
    d = dict([('first name', 'Andrey'), ('last name', 'Andreiev'), ('age', 25)])
    print(d)
    d = dict()
    # менее популярный вариант, но вполне допустимый
    d['first name'] = 'Andrey'
    d['last name'] = 'Andreiev'
    d['age'] = 25
    # поэлементно задаються ключи и массово задаются значения
    d = dict.fromkeys(['name one', 'name two', 'name three'], 5)
    print(d)
    # массово задаются ключи с пустыми значениями
    d = dict.fromkeys(['name one', 'name two', 'name three'])
    print(d)

    # dict comprehension
    thousand_dict = {i: i for i in range(len_to_test)}