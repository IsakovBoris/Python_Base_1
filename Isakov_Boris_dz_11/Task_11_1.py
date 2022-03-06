from datetime import datetime


class Date:
    def __init__(self, date):
        self.date = date


    @classmethod
    def result_date(cls, date):
        if Date.validation(date):
            date = date.replace('-', ',')
            dates_list = (date.split(','))
            result_date = []
            for days in dates_list:
                result_date.append(int(days))
            return tuple(result_date)



    @staticmethod
    def validation(date):
        try:
            return datetime.date(datetime.strptime(date, '%d-%m-%Y'))
        except ValueError:
            raise ValueError('Введен неверный формат даты. Необходимо ввести дату в формате "дд-мм-гггг"')


if __name__ == '__main__':
    dates=('01-03-2022','01-13-2022','32-03-2022','01/03/2022')
    for date in dates:
        print(date)
        try:
            print(f'Результат: {Date.result_date(date)}')
        except ValueError as error:
            print(f'Ошибка: {error}')
