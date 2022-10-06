import json
from pprint import pprint
# pretty print
from uuid import uuid4
# unique user id (uuid4 генерирует уникальный случайный ключ фиксированной длины)


def display_student_data(d: dict) -> str:
    """
    Читабельно и репрезентативно формирует строку для вывода полных данных об одном студенте
    :param d: полные данные об одном студенте
    :return: возвращает сформированную строку о студенте
    """
    return f'{d["full name"]} studying on {d["faculty"]} faculty in group #{d["group"]}'


def view_index(index_name: str, index_to_view: dict, source_uid_data: dict):
    """
    Функция выводит на экран в читебальном репрезентативном виде
    студентов, разделенных по признаку index_name (в index_to_view)
    :param index_name: название нашего индекса для вывода
    :param index_to_view: сам индекс, словарь списком.
        Ключи словаря - уникальные значения в индексе
        значения словаря - списки уникальных айдишников студентов (ссылки на полные данные)
    :param source_uid_data: полные данные студентов промаркированные своим уникальным айдишником
    :return: ничего
    """
    print(f'Students by {index_name.capitalize()}')
    for key, values in index_to_view.items():
        print(f'Displaying {key} students:')
        for uid in values:
            print(f'  {display_student_data(source_uid_data[uid])}')


data = json.load(open('students.json', mode='r'))

# индекс всех студентов, реализуется посредством создания уникального айдишника для каждого студента
uid_index = dict()
# создаём предметные указатели/группируем по GROUP BY/создаём индекс по Факультетам и по Группам
# ключи словаря - это уникальные названия факультетов
# значения - это список студентов. Если хранить полную копию данных на студента:
#   объём данных невероятно растёт
#   изменение данных. Нужно найти каждую копию и в каждой копии тогда нужно поменять данные (слишком много изменений)
# поэтому создаются ссылки на данные, данные же хранятся 1 раз
faculty_index = dict()
group_index = dict()
# проходимся по данным каждого студента
#   чтобы дать каждому уникальный айди
#   чтобы включить его в нужные указатели/индексы (факультет и группа)
for student_data in data['students']:
    # присваиваем каждому студенту уникальный айди
    student_data['uid'] = str(uuid4())
    # заполняем полное имя студента
    student_data['full name'] = f"{student_data['first name']} {student_data['last name']}"
    # индекс это как предметный указатель в любой технической литературе
    # добавляем ссылку на полные данные студента в индекс айдишников
    uid_index[student_data['uid']] = student_data
    # формируем индекс факультетов
    # если уже факультет есть в перечне указателя (индекса), то мы добавляем студента в эту группу
    if student_data['faculty'] in faculty_index:
        faculty_index[student_data['faculty']].append(student_data['uid'])
    # если факультета нет в перечне указателя (индекса), то мы создаём поле под множество студентов
    # и добавляем нашего первого студента туда
    else:
        faculty_index[student_data['faculty']] = list()
        faculty_index[student_data['faculty']].append(student_data['uid'])

    # всё аналогично для второго индекса
    if student_data['group'] in group_index:
        group_index[student_data['group']].append(student_data['uid'])
    else:
        group_index[student_data['group']] = list()
        group_index[student_data['group']].append(student_data['uid'])
# выводим все данные (списком)
pprint(data)
# выводим все данные (индексом уникальных айди)
pprint(uid_index)

# просмотр в разрезе факультета
view_index('факультет', faculty_index, uid_index)

print('#' * 10)

# просмотр в разрезе группы
view_index('группа', group_index, uid_index)

# сохраняем данные о студентах в формате списка
json.dump({'students': list(uid_index.values())}, open('students.json', 'w'), indent=4)
json.dump(faculty_index, open('faculty_index.json', 'w'), indent=4)
json.dump(group_index, open('group_index.json', 'w'), indent=4)
