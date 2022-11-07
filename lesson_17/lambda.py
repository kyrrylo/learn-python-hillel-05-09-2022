from random import randint
from uuid import uuid4
import os


x = [{"name": str(uuid4()), "rank": randint(1, 20)} for i in range(10)]
print(x)


def get_rank(d: dict):
    return d["rank"]


print(sorted(x, key=get_rank, reverse=True))

# lambda - или анонимные функции
print(sorted(x, key=lambda y: y["rank"], reverse=True))
print(min(x, key=lambda y: y["rank"]))
print(max(x, key=lambda y: y["rank"]))

# синтаксис конструкции lambda-функция
# lambda arg1, arg2, arg3, arg4...argn: *то что возвращаем*
# функция в одну строчку, однако можно добавить условие такого типа (в одну строчку):
# z = True if 5 > 0 else False

# примеры использования lambda
list_z = [randint(1, 20) for i in range(10)]
print(list_z)
print(list(filter(lambda z: z > 5, list_z)))

# filter(
# "функция, возвращающая да или нет",
# "итерируемый объект, элементы которого подаются функцией на проверку"
# )

# то же самое, что filter функция, однако чуть медленнее и даёт большую нагрузку на память для больших списков
list_z = [randint(1, 20) for i in range(10)]
list_z = [z for z in list_z if z > 5]

filenames = [os.path.join('..', 'lesson_14_15_16', filename) for filename in os.listdir(os.path.join('..', 'lesson_14_15_16'))]
print(filenames)
filtered_filenames = list(filter(os.path.isfile, filenames))
print(filtered_filenames)
file_extensions = list(map(lambda s: s[s.rfind('.'):], filtered_filenames))
print(file_extensions)
