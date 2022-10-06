filenames = [
    'hfdja.txt',
    'my.best.image.png',
    'main.py',
    'data.json',
    'data.json.zip'
]

# file extension - расширение файла, его тип, сокращение после точки в конце файла
my_string = 'g.exe'
dot_index = my_string.rfind('.')  # rfind возвращает индекс первого попавшегося искомого элемента, но ищет с правой стороны
print(dot_index)
print(my_string[dot_index + 1:])

for fname in filenames:
    fname_extension = fname[fname.rfind('.') + 1:]
    print(f'Filename: {fname} is with extension: {fname_extension}')

with open('my_file.txt') as f:
    our_text = f.read()
    # split() - разделяет строку на список по пробелам, \t и \n (whitespace)
    # splitlines() - разделяет строку на список строк по \n
    list_of_lines = list()
    for line in our_text.splitlines():
        line = line.split(',')
        list_of_phrases = list()
        for phrase in line:
            list_of_phrases.append(phrase.strip())
        # join - объединяет список строк в одну
        list_of_lines.append("--".join(list_of_phrases))
    print(';\n'.join(list_of_lines))
    # strip - раздеть
    our_text.strip()  # убрать повторяющиеся символы с обоих сторон
    our_text.rstrip()  # только справа
    our_text.lstrip()  # только слева

with open('my_file.txt') as f:
    strip_results = list()
    rstrip_results = list()
    lstrip_results = list()
    for line in f.readlines():
        strip_results.append(line.strip('?!. \n\tabeBA'))
        rstrip_results.append(line.rstrip('?!. \n\tabeBA'))
        lstrip_results.append(line.lstrip('?!. \n\tabeBA'))
    print('Strip results:', '\n'.join(strip_results), sep='\n')
    print('Right strip results:', '\n'.join(rstrip_results), sep='\n')
    print('Left strip results:', '\n'.join(lstrip_results), sep='\n')
