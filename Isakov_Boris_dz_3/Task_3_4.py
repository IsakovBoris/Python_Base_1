def repeats(list_in):  # Функция для исключения повторов в списке имен
    list_out = []
    for i in list_in:
        if i not in list_out:
            list_out.append(i)
    return list_out

def thesaurus_adv(*args) -> dict:
    args_list=repeats(list(args))
    args_list.sort(key=lambda name: name.split()[::-1])  # Сортировка элементов списка в алфавитном порядке (Фамилия, Имя) - альтернативный вариант вывода отсортированного итогового словаря
    dict_out = {}
    family_name_key = [] # Список ключей по первым буквам имени и фамилии для словаря на выходе
    i = 0
    while i < len(args_list):  # Цикл перебора элементов в списке имен
        for indx in args_list[i]:
            if indx.isupper() == True:
                family_name_key.append(indx)
        family_key=family_name_key[1]  # Ключ для словаря верхнего уровня
        name_key = family_name_key[0]  # Ключ для вложенного словаря
        name = args_list[i]  #  Переменная для подстановки имени в словарь
        for key in dict_out:  #  Цикл для дополнения вложенных словарей именами по записанным ранее ключам в словарь верхнего уровня
            if family_key == key:
                exhist_name=dict_out.get(key)  #  Переменная для изменения записанного ранее вложенного словаря
                exhist_name.setdefault(name_key,[]).append(name)  #  Изменение вложенного словаря
                dict_out.setdefault(family_key, {name_key: [{name_key:[name]}]})
        dict_out.setdefault(family_key, {name_key: [name]})
        family_name_key.clear()  # очистка списка ключей для подбора новых значений ключей на следующем повторении цикла
        i +=1
    result = sorted(dict_out.items())  # сортировка словаря по ключу согласно заданию
    return dict(result)

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Инна Серова"))
