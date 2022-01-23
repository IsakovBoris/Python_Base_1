def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []  # Итоговый список приветсвий согласно заданию
    i = 0  # Индекс для перебора элементов списка
    while i < len(list_in):  # Цикл для извлечения имени из списка
        reversed_string = my_list[i][::-1] #Разворачиваем каждую строку в списке
        space_search = reversed_string.find(' ')  #Находим индекса пробела следующего после каждого имени в развернутой строке
        reversed_name = reversed_string[0:space_search]  #Выносим из строки имя
        name = reversed_name[::-1]  #Разворачиваем имя в правильном порядке букв
        clear_name = name.capitalize()  # Применяем функцию capitalize для правильного написания имени
        list_out.append(f'Привет, {clear_name}!') # Вносим в итоговый список имя с приветсвием согласно условию задания
        i += 1
    return list_out

my_list = ['инженер- Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита',]
result = convert_name_extract(my_list)
print(result)
