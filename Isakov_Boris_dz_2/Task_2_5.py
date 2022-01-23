from random import uniform

def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    str_out = str()  # Строка для записи цен
    i = 0  # Индекс для перебора элементов входного списка
    while i < len(list_in): # Цикл перебора элементов списка
        Rubles = int(list_in[i])  # Переменная в которую записывается целая часть элемента из списка
        Pennies = int((round(list_in[i] - int(list_in[i]), 2) * 100)) # Переменная в которую записывается цифры после точки элемента из списка
        Rubles_str = str(Rubles) # Приведение полученных результатов в строковому типу для записи в итоговую строку и допостановки 0 для чисел меньше 10
        Pennies_str = str(Pennies)
        if Rubles < 10: # Условие проверки результата если он меньше 10
            Rubles_str = Rubles_str.zfill(2)
        if Pennies < 10:
            Pennies_str = Pennies_str.zfill(2)
        if i == 0:  # Условие записи первого элемента в строку без лишних пробелов в начале строки
            str_out = f'{Rubles_str} руб {Pennies_str} коп,'
        elif i == len(list_in) - 1:  # Условие записи последнего элемента для окончание точкой итоговой строчки
            str_out = f'{str_out} {Rubles_str} руб {Pennies_str} коп.'
        else:  # Условие записи остальных элементов в строку
            str_out = f'{str_out} {Rubles_str} руб {Pennies_str} коп,'
        i += 1
    return str_out

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print("Итоговая строка:")
print(result_1)

def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_in_sort = list_in.sort()  # Операция по сортировке исходного листа по принципу in_place
    return list_in


# Информация по исходному списку my_list
print('Id исходного листа:',id(my_list))
result_2 = sort_prices(my_list)
# Доказательство, что результат result_2 остался тем же объектом
print("Отсортированный результирующий список:")
print(result_2)
print('Id отсортированного листа:', id(result_2))


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in,reverse=True) # Операция по сортировке исходного листа по принципу not_in_place
    return list_out

result_3 = sort_price_adv(my_list)
print("Cписок элементов в списке по убыванию:")
print(result_3)

def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = sort_prices(list_in)[:(len(list_in)-6):-1] # Операция по сортировке исходного листа согласно функции sort_prices может применяется, если ранее данная функция не вызывалась
    return list_out  # В списк попадает срез из отсортированного входного списка с конца до 5 элемента с конца, независимо от длины входного списка

result_4 = check_five_max_elements(my_list)
print("список из пяти самых больших элементов:")
print(result_4)
