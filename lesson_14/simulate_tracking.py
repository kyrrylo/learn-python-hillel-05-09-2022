from chief import Chief
from security import Security
from waiter import Waiter
from random import choice, random
from time import sleep
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',)

if __name__ == '__main__':
    # наше заведение
    location_list = [
        "Технический Сан-Узел",
        "Кухня",
        "Склад",
        "Охранная будка",
        "Зона отдыха (курилка)",
        "Зона клиентов"
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
