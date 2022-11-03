import datetime
import json
from employees import Chief, Security, Waiter
from pprint import pprint


class SimulationAnalyzer:
    def __init__(self, log_filename: str):
        self._log_filename = log_filename
        self._parsed_log = list()
        self._employees = dict()
        self._location_index = dict()
        self._position_index = dict()
        self._name_index = dict()

    @property
    def employees(self):
        return self._employees

    def read_log(self, export_to_json: bool = False):
        """
        Производит чтение и парсинг лога, сохранение всех событий и действующих лиц в поля класса:
            _parsed_log - список событий
            _employees - словарь действующих лиц (по имени)
        :param export_to_json: если True, экспортирует спаршенный лог в джсон формате
        """
        # парсим лог событий
        with open(self._log_filename) as f:
            for line in f.readlines():
                # разделяем события на дату, тип сообщения, должность работника, позицию и посещенную зону
                dt, msg_importance, position, name, location = line.split(' - ')
                # конвертируем дату в объект
                dt_object = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S,%f')
                if name not in self._employees:
                    if position == 'Chief':
                        obj = Chief(name)
                    elif position == 'Security':
                        obj = Security(name)
                    elif position == 'Waiter':
                        obj = Waiter(name)
                    else:
                        raise NotImplementedError(f'Должность {position} не указана в реестре доступных')
                    self._employees[name] = obj

                # добавляем распаршенную инфу в список для анализа
                self._parsed_log.append({
                    "datetime": dt_object,
                    "message_importence": msg_importance.strip(),
                    "position": position.strip(),
                    "name": name.strip(),
                    "location": location.strip(),
                    "str": line.strip()
                })
        if export_to_json:
            json.dump(self._parsed_log, open('parsed_log.json', 'w'), indent=4, ensure_ascii=False)

    def _indice_by_field(self, field_name: str, field_object: dict) -> dict:
        # checking if not empty
        if field_object:
            field_object = dict()
        for row in self._parsed_log:
            if row[field_name] in field_object:
                field_object[row[field_name]].append(row)
            else:
                field_object[row[field_name]] = list()
                field_object[row[field_name]].append(row)
        return field_object
    
    def indice_by_location(self) -> dict:
        return self._indice_by_field('location', self._location_index)

    def indice_by_name(self) -> dict:
        return self._indice_by_field('name', self._name_index)
    
    def indice_by_position(self) -> dict:
        return self._indice_by_field('position', self._position_index)

    def time_spent_in_location_by_name(self, name: str) -> dict:
        if name not in self._name_index:
            raise KeyError(f'Employee named {name} not found!')
        # время проведенное в рабочих локациях
        work_time = 0.0
        # время проведенное в нерабочих и незапрещенных локациях
        relax_time = 0.0
        # время проведенное в запрещенных локациях
        dangerous_time = 0.0
        # previous fields
        name_index = self._name_index[name]
        first_event, remaining_index = name_index[:1][0], name_index[1:]
        prev_location = first_event['location']
        prev_time = first_event['datetime']
        employee = self._employees[name]
        for event in remaining_index:
            time_spent_seconds = (event['datetime'] - prev_time).total_seconds()
            if prev_location in employee.working_locations:
                work_time += time_spent_seconds
            elif prev_location in employee.unavailable_locations:
                dangerous_time += time_spent_seconds
            else:
                relax_time += time_spent_seconds
            prev_location = event['location']
            prev_time = event['datetime']
        time_spent_report = {
            "employee_name": name,
            "employee_position": employee.position,
            "working_time": work_time,
            "relax_time": relax_time,
            "prohibited_time": dangerous_time
        }
        return time_spent_report


    @staticmethod
    def view_index(index_name: str, index_to_view: dict):
        """
        Функция выводит на экран в читебальном репрезентативном виде
        студентов, разделенных по признаку index_name (в index_to_view)
        :param index_name: название нашего индекса для вывода
        :param index_to_view: сам индекс, словарь списком.
            Ключи словаря - уникальные значения в индексе
            значения словаря - списки уникальных айдишников студентов (ссылки на полные данные)
        :return: ничего
        """
        print(f'События группированные по {index_name.capitalize()}')
        for key, values in index_to_view.items():
            print(f'Отображаем {key} события:')
            for row in values:
                print(row['str'])


if __name__ == '__main__':
    analyzer = SimulationAnalyzer('logs/2022-10-31.log')
    analyzer.read_log()
    analyzer.view_index('Локация', analyzer.indice_by_location())
    analyzer.view_index('Должность', analyzer.indice_by_position())
    analyzer.view_index('Имя', analyzer.indice_by_name())

    working_time = list()
    for name, employee_obj in analyzer.employees.items():
        report = analyzer.time_spent_in_location_by_name(name)
        print(report)
        working_time.append(report)
    pprint(sorted(working_time, key=lambda x: x['working_time'], reverse=True))
