import locations
from chief import Chief
from security import Security
from waiter import Waiter
from random import choice, random
from time import sleep
import logging
import os
import datetime

# / - войти в папку на линуксе и на маке
# \ - войти в папку на виндовс
# чтобы наш код был мультиплатформенным, нужно пользоваться библиотекой os.path.
# Метод join позволяет объединять все элементы пути (корневая папка, подпапка, следующая подпапка, название файла)
fh = logging.FileHandler(os.path.join('logs', datetime.date.today().strftime('%Y-%m-%d.log')))
sh = logging.StreamHandler()
logging.root.addHandler(fh)
logging.root.addHandler(sh)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)


if __name__ == '__main__':
    # наше заведение
    location_list = [
        locations.client_zone.ClientZone.name,
        locations.kitchen.Kitchen.name,
        locations.security_room.SecurityRoom.name,
        locations.smoking_room.SmokingRoom.name,
        locations.warehouse.Warehouse.name,
        locations.wc.WC.name
    ]

    # его работники
    employee_list = list()
    employee_list.append(Security('John'))
    employee_list.append(Security('Mark'))
    employee_list.append(Waiter('Mike'))
    employee_list.append(Waiter('Julia'))
    employee_list.append(Waiter('Sophia'))
    employee_list.append(Waiter('Neil'))
    employee_list.append(Chief('Lora'))

    #
    while True:
        # выбираем случайного работника
        acting_employee = choice(employee_list)
        # выбираем случайную локацию
        location = choice(location_list)
        # используем ключ-карту в этой локации
        acting_employee.check_in(location)
        # ждём от 1 до 6 секунд (случайное время)
        sleep(random() * 5 + 1)


"""
подсказка для последнего домашнего
menu = list()
    for row in all_rows_in_json_or_csv_file:
        if row['category'] == 'TV':
            obj = TV()
        elif row['category'] == 'Headset':
            obj = Headset()
        menu.append(obj)
        
    filter = ('category', 'TV')
    filtered_objects = list()
    if filter[0] == 'category':
        for obj in menu:
            if obj.category == filter[1]:
                filtered_objects.append(obj)
"""
