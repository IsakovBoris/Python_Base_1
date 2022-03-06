class DivisionExceprion(ValueError):
    def __init__(self, message):
        self.txt = message


def check_division(number):
    try:
        number = float (number)
    except ValueError:
        raise DivisionExceprion('Для деления необходимо ввести числа')
    if number == 0:
        raise DivisionExceprion('Деления на ноль недопустимо')
    return number


if __name__ == '__main__':
    print(('Введите числа для деления. Для завершения операции введите "stop" '))
    while True:
        dividend = input('Введите Делимое: ')
        if dividend == 'stop':
            break
        divider = input('Введите Делитель: ')
        if divider  == 'stop' :
            break
        try:
            print(f'Результат: {round(check_division(dividend)/check_division(divider),2)}')
        except DivisionExceprion as error:
            print(f'Ошибка: {error}')
