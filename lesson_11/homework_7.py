"""
Написати програму, для ведення та перегляду нотаток. Програма пропонує користувачу вводити ключові слова, та опрацьовує їх. Перелік ключових слів:

add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
earliest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшоїдо найдовшої


Якщо довжина нотаток однакова, то їх порядок відображення не принциповий.
"""
import os


FILENAME_FOR_NOTES = 'notes.txt'


def save(notes: list):
    notes_text = list()
    for data in notes:
        notes_text.append(data[0])
    # notes_text = [x[0] for x in notes]
    with open(FILENAME_FOR_NOTES, 'w') as f:
        f.write('\n'.join(notes_text))
    print(f'{len(notes)} notes have been successfully written to {FILENAME_FOR_NOTES}')


def load(new_notes: list) -> list:
    """
    Функція приймає нові нотатки, завантажує із файлу збережені раніше нотатки та
    повертає хронологічно вірний список усіх цих нотаток
    :param new_notes:
    :return:
    """
    all_notes = list()
    try:
        with open(FILENAME_FOR_NOTES, 'r') as f:
            for note in f.readlines():
                # отрезаем символ переноса строки
                note = note.strip('\n')
                # считаем длину
                note_len = len(note)
                # добавляем данные о заметке
                all_notes.append((note, note_len))
    except Exception:
        print(f'File {FILENAME_FOR_NOTES} was not found, cannot load notes')
        return new_notes
    all_notes_len = len(all_notes)
    print(f'Successfully loaded {all_notes_len} notes from {FILENAME_FOR_NOTES}, '
          f'now you have {all_notes_len + len(new_notes)} notes.')
    for data in new_notes:
        all_notes.append(data)
    # extend - расширить
    # all_notes.extend(new_notes)
    return all_notes


def add(notes: list):
    """
    :param notes: copy of global scope notes list
    :return:
    """
    note = input('Please, enter your note: ')
    note_len = len(note)
    notes.append((note, note_len))
    return notes


def alternative_add() -> tuple:
    """
    :return:
    """
    note = input('Please, enter your note: ')
    return (note, len(note))


def earliest(notes: list):
    """
    :param notes:
    """
    # notes[::-1] reverse for latest
    for data in notes:
        print(data[0])
    # "\n".join(notes)


def longest(notes: list):
    """
    :param notes:
    """
    def by_len(d):
        return d[1]
    # sorted(notes, key=lambda data: data[1], reverse=True)
    # возьми данные о каждой заметке (сортированные по длине в обратном порядке),
    # в данных возьми поле по имени note и выведи его на экран
    for data in sorted(notes, key=by_len, reverse=True):
        print(data[0])
    # "\n".join(notes)


def info():
    """
    Ця функція виводить на екран підказку як користуватись програмою
    """
    print('''Expected command list:
    add
    earliest
    latest
    longest
    shortest
    save
    load
    ''')


if __name__ == '__main__':
    info()
    source_notes = list()
    while True:
        user_input = input('>')
        if user_input == 'add':
            source_notes = add(source_notes)
        elif user_input == 'alternative_add':
            source_notes.append(alternative_add())
        elif user_input == 'earliest':
            earliest(notes=source_notes)
        elif user_input == 'save':
            save(notes=source_notes)
        elif user_input == 'load':
            source_notes = load(source_notes)
        elif user_input == 'latest':
            pass
        elif user_input == 'longest':
            longest(notes=source_notes)
        elif user_input == 'shortest':
            pass
        elif user_input == 'exit':
            print('Thanks, bye')
            break
        else:
            info()
