def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
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
    if value.istitle() == True:
        value=value.lower()
        str_out = dict_translate.get(value)
        if str_out == None:
            return str_out
        else:
            return str_out.title()
    else:
        str_out = dict_translate.get(value)
        return str_out


print(num_translate_adv("One"))  # Один
print(num_translate_adv("eight"))  # восемь
print(num_translate_adv("Five"))  # Пять
print(num_translate_adv("Twelve"))  # None
print(num_translate_adv("fifty"))  # None
