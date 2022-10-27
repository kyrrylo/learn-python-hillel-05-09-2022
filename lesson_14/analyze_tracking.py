import datetime
import json


if __name__ == '__main__':
    parsed_log = list()

    # парсим лог событий
    with open('tracked_info.log') as f:
        for line in f.readlines():
            # разделяем события на дату, тип сообщения и само сообщение
            dt, msg_importance, message = line.split(' - ')
            # конвертируем дату в объект
            dt_object = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S,%f')
            # разделяем сообщение на должность, имя, *сообщение* и локацию
            position, name, _, location = message.strip().split('::')
            # добавляем распаршенную инфу в список для анализа
            parsed_log.append({
                "datetime": dt,
                "position": position.strip(),
                "name": name.strip(),
                "location": location.strip()
            })

    json.dump(parsed_log, open('parsed_log.json', 'w'), indent=4, ensure_ascii=False)

    # TODO сделать индекс по локации, по должности и по имени
    # на каждого работника можно сгрупировать локации и сумарное время пребывания в них
    # в зависимости от должности ставить флаг рабочая/нерабочая локация
    # сценарии альтернативного реагирования по попытку чек-ин в разных локациях (охранник не может войти на Кухню н-р)
    # разные уровни логирования в зависимости от пары должность + локация
