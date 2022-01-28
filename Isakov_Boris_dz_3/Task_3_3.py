def repeats(list_in):  # Функция для исключения повторов в списке имен
    list_out = []
    for i in list_in:
        if i not in list_out:
            list_out.append(i)
    return list_out


def thesaurus(*args) -> dict:
    args_list=repeats(list(args))
    dict_out ={}
    for i in range (0, len(args_list)):
        key_name = args_list[i][0]
        name = args_list[i]
        dict_out.setdefault(key_name,[]).append(name)
    result=sorted(dict_out.items())
    return dict(result)


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
