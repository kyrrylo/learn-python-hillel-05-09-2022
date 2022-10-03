import time

# Pointer - указатель
# File Pointer (fp) - указатель на файл
# with (вместе с) "функция, открывающая указатель на файл" as (под именем) "имя переменной-указателя"
with open('my_file.txt') as fp:
    print(fp)
    print(type(fp))
    print(f'{fp.readable()=}')  # readable - читабельный, можно ли читать
    print(f'{fp.writable()=}')  # writable - можно ли записывать

    # wrapper - обёртка
    # IO - input/output ввод/вывод
    # \n - служебный символ переноса строки

    # чтение всего файла
    text = fp.read()
    print(type(text), text)

    # seek - поиск, искать
    # seek - устанавливает место (закладка) с которого идёт чтение файла
    fp.seek(0)
    # чтение всего файла с разбивкой на строки
    lines = fp.readlines()
    print(type(lines), lines)

    fp.seek(0)
    # чтение файла построчно (по строке за вызов)
    line = fp.readline()
    while line:
        print(type(line), line)
        line = fp.readline()
        time.sleep(1)

    # EOF - end of file пайтон возвращает пустую строку только тогда, когда достигнут конец файла (на чтении символ EOF)
