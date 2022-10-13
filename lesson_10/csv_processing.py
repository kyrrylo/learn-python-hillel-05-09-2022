# csv file - comma separated values
# значения, разделённые запятой
import csv
import sys
# delimeter - запятая в csv файле, разделяет поля на колонки
# quotechar - кавычки в csv файле, символ экранирования

future_csv_data = list()

with open('my_csv_file.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
     print('Size of csv reader:', sys.getsizeof(spamreader))
     for i, row in enumerate(spamreader):
         print(f'{i} row')
         print(row)
         future_csv_data.append(row)

print('Size of rows:', sys.getsizeof(future_csv_data))


print('#' * 50)
future_csv_dict_data = list()
with open('my_csv_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(row)
        future_csv_dict_data.append(row)

print('#' * 50)
with open('custom_csv_file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        print(row)

# pandas - расширенный модуль для работы с csv-файлами (и более)

with open('csv_writer_check.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    for row in future_csv_data:
        spamwriter.writerow(row)
    spamwriter.writerow(['this\nwas', 'written by', 'csv,writer', 'method'])


with open('csv_dict_writer_check.csv', 'w', newline='') as csvfile:
    if future_csv_dict_data:  # если наши данные не пустые
        fieldnames = list(future_csv_dict_data[0].keys())
    else:
        fieldnames = list()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # записываем наши названия колонок
    for row in future_csv_dict_data:
        writer.writerow(row)
    writer.writerow({'last name': 'I dont know'})

with open('csv_dict_writer_check.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
