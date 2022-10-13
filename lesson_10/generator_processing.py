import sys
import time

def gen_vs_list():
    # int, float
    # str
    # bool
    # list, dict
    # def return
    # generator yield
    xlist = [i for i in range(100)]
    print('xlist size:', sys.getsizeof(xlist))
    xgen = (i for i in range(100))
    print('xgen size:', sys.getsizeof(xgen))
    print(xlist)
    print(xgen)
    for element in xlist:
        print(element, end=' ')
    print()
    for element in xgen:
        print(element, end=' ')
    print()


def simple_generator_example():
    def my_generator_function(list_to_convert: list):
        for x in list_to_convert:
            print(f'1 about to generate {x}')
            yield x
            print(f'3 just generated {x}')

    our_list = [x for x in range(5)]
    for element in my_generator_function(our_list):
        print(2, element)


def fibonacci_generator(a=0, b=1):
    # a-b-c
    while True:
        yield a
        c = a + b
        a = b
        b = c


def fibonacci_example():
    for fibonacci_number in fibonacci_generator():
        print(fibonacci_number)
        time.sleep(0.5)


def read_file_generator(filename, bytes=500):
    """
    Возвращает до :bytes: символов текста из файла
    Не разрывает слова, делит по строкам или по пробелам (если попалась длинная строка)
    :param filename: имя файла
    :param bytes: размер чтения
    :return: генерирует текст из файла (по логике описанной выше)
    """
    with open(filename) as fp:
        text = fp.read(bytes)
        buffer = ''
        while text:
            # соединяем буфер и свежие данные из файла
            text = buffer + text
            # опустошаем содержимое буфера
            buffer = ''
            # сначала мы найдём последний перенос строки (rfind)
            split_index = text.rfind('\n')
            # если такого нет, найдём последний пробел (rfind)
            if split_index == -1:
                split_index = text.rfind(' ')
            # если и такого нет, то возвращаем текст как есть
            if split_index == -1:
                yield text
                # сгенерировать
                # врожай
            # если же мы нашли перенос строки или пробел, то мы можем отрезать всё, что правее него (после)
            else:
                yield text[:split_index]
                # и сохранить в буфер. Буфер будет началом следующего чтения из файла
                buffer = text[split_index:]
            # читаем новые данные, но не 500 байт, а меньше на длину буфера
            text = fp.read(bytes - len(buffer))
        yield buffer


def read_file_example():
    all_file_data = str()
    gen_object = read_file_generator('my_csv_file.csv')
    # ключевое слово next достаёт значения генерируемые yield
    # знать о ключевом слове нужно, а вот делать так не стоит - только в качестве теста
    portion = next(gen_object)
    print(portion)
    print('=' * 10)
    for portion in gen_object:
        print(portion)
        print('#' * 10)
        all_file_data += portion

    print('File data size:', sys.getsizeof(all_file_data))
    print('File data size:', sys.getsizeof(read_file_generator('my_csv_file.csv')) + sys.getsizeof(portion))


if __name__ == '__main__':
    # gen_vs_list()
    # simple_generator_example()
    # fibonacci_example()
    read_file_example()


# знать надо, делать не надо
def my_f(local_m):
    local_m = local_m + '5678'
    return local_m


m = '32'
# пример правильного обмена данными между глобал скоупом и функцией
# представим, что глобал скоуп - это мы, а функция - это мастер
# данные - это изделие, над которым мастер должен сделать свою часть работы
# для этого нужно изделие выслать мастеру, это время мы будем его ожидать, а потом получить обратно изменённое изделие
# my_f(m) - отправка изделия мастеру
# def my_f(local_m): - получение изделия мастером
# тело функции - работа мастера над изделием
# return local_m - отправка изделия мастером к нам
# m = - получение изделие нами от мастера
m = my_f(m)
print(m)
