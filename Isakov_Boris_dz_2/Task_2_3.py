def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    ips = 0  # Индекс для перебора входящего списка, сокращение от index per search
    while ips < len(list_in):  # Цикл для поиска чисел в списке и подстановки кавычек по бокам от этих чисел обратно в список
        try:  # Применяю приведение каждого элемента к типу int и конструкцию обработки исключений в случаях когда элемент не может быть приведен к данному типу
            element = list_in[ips]  # Переменная для подстановки значения элемента
            e_check = int(list_in[ips]) # Переменная в которую записывается числовой элемент с типом int
            list_in.insert(ips, '"')  # Добавляем по бокам кавычки от элемента содержащий число
            list_in.insert((ips + 2), '"')
            if e_check < 10:  # условие при котором добавляется 0 к числу в списке
                list_in.remove(element) # удаление элемента
                if element[0] == '+' or element[0] == '-':  # проверка элемента на наличие знаков + или -
                    decimal_number = element.zfill(3)  # применение строкового метода дополнения нулями строки до указаной длины
                else:
                    decimal_number = element.zfill(2)
                list_in.insert(ips + 1, decimal_number)  # Возвращяем измененный элемент в изначальный список
            ips += 2  # при нахождении подходящего элемента увеличиваем шаг увелечения индекс проверки чтобы перескочить элемент с числом, позиция которого стала +1
        except ValueError: # при ошибке операции int пропускаем все действия, увеличиваем индекс перебора и заходим снова в цикл
            pass
        finally:
            ips += 1

    indx = 0  # новый индекс для перебора измененного списка и подставления элементов строку
    str_out = str()  # итоговая строка в которую записывается результат
    while indx < len(list_in):  # цикл для перебора элементов и правильного расставления пробелом между ними в строке
        if list_in[indx] == '"':  # при проверке следующих элементов при нахождении первых ковычек записываем в строку число и кавычки по бокам без пробелов
            if indx == 0: # если первый элемент списка кавычки, тогда записываем сразу три элемента без пробелов в начале и между кавычками с числом
                str_out=f'{list_in[indx]}{list_in[indx + 1]}{list_in[indx + 2]}'
            else:
                str_out = f'{str_out} {list_in[indx]}{list_in[indx + 1]}{list_in[indx + 2]}'
            indx += 2  # увеливаем индекс перебора чтобы перескочить сложенные ранее элементы
        else:  # при проверке элементов без кавычек
            if indx == 0:  #если первый элемент без кавычек, тогда записываем его в строку без пробелов перед элементом
                str_out = f'{list_in[indx]}'
            else:
                str_out = f'{str_out} {list_in[indx]}'  # остальные элементы записываются с одинарным пробелом
        indx += 1
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)