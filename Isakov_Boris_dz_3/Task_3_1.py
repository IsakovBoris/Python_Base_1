def num_translate(value: str) -> str:
    """Переводит числительное с английского на русский.
    Записываем словарь с парами значений для перевода.
    Запись произведена внутри функции, так как при импорте функции в другой модуль
    вместе с функцией импортируются и значения словаря
    """
    dict_translate = {
        "one": 'один',
        "two": 'два',
        "three": 'три',
        "four": 'четыре',
        "five": 'пять',
        "six": 'шесть',
        "seven": 'семь',
        "eight": 'восемь',
        "nine": 'девять',
        "ten": 'десять'
    }
    str_out = dict_translate.get(value)
    return str_out


print(num_translate("one"))  # один
print(num_translate("eight"))  # восемь
print(num_translate("eleven"))  # None
