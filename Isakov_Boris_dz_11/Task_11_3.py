class CheckNumber(ValueError):
    def __init__(self, message):
        self.txt = message

def check_value(number):
    try:
        number = float(number)
    except ValueError:
        raise CheckNumber('Необходимо вводить только числа!')
    return number


if __name__ == '__main__':
    print(('Введите числа. Для завершения операции введите "stop" '))
    result_list=[]
    while True:
        number = input('Введите число: ')
        if number == 'stop':
            break
        try:
            result_list.append(check_value(number))
        except CheckNumber as error:
            print(f'Ошибка: {error}')
    print(result_list)
