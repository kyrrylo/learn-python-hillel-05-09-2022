# library - сторонняя библиотека, которая открывает новый функционал
import datetime
import logging
import time


def datetime_intro():
    # v - Variable
    # c - Class
    x = datetime.datetime.now()
    print(x)
    print(x.year, x.month, x.day, x.hour, x.minute, x.second, x.microsecond)
    # strftime (f = from) создаёт строку из объекта datetime
    datetime_format = '%d/%b/%Y %H:%M:%S.%f'
    datetime_string = x.strftime(datetime_format)
    print(datetime_string)
    # time.sleep(0.5)
    # strptime создаёт объект datetime из строки
    y = datetime.datetime.strptime(datetime_string, datetime_format)
    print(type(y), y)
    print('#' * 10)
    # timedelta - разница во времени
    now = datetime.datetime.now()
    datetime.datetime(2022, 10, 27, 19, 35, 50, 123)
    # seven_days = datetime.timedelta(hours=24 * 7)
    # seven_days = datetime.timedelta(weeks=1)
    # seven_days = datetime.timedelta(days=7)
    # seven_days = datetime.timedelta(minutes=60 * 24 * 7)
    seven_days = datetime.timedelta(seconds=60 * 60 * 24 * 7)
    print(type(seven_days), seven_days)
    seven_days_ago = now - seven_days
    print(type(seven_days_ago), seven_days_ago)
    if now > seven_days_ago:
        print(f'{now} is later than {seven_days_ago}')
    else:
        print(f'{now} is earlier than {seven_days_ago}')

    time_object = datetime.time(hour=19, minute=40, second=30)
    date_object = datetime.date(year=2022, month=10, day=27)
    print(time_object, type(time_object))
    print(date_object, type(date_object))
    datetime_custom_made = datetime.datetime.combine(date_object, time_object)
    print(datetime_custom_made, type(datetime_custom_made))
    print(datetime_custom_made.date(), type(datetime_custom_made.date()))
    print(datetime_custom_made.time(), type(datetime_custom_made.time()))


def logging_intro():
    # verbosity (общительность/многословность)
    # levels of verbosity: CRITICAL, ERROR, WARNING, INFO, DEBUG
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',)
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')
    logging.error('Don\'t forget about me')


if __name__ == '__main__':
    # datetime_intro()
    logging_intro()
