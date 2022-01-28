import random
from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    i = 0
    list_out = []
    while i < count:
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        i += 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))


def get_jokes_adv(count: int, repeats: bool) -> list:
    """Возвращает список шуток в количестве count
    :count: количество шуток
    :repeats: условие повторения или оригинальности слов в шутках
    """
    if count > len(nouns):
        print('максимальное количество оригинальных шуток:', len(nouns))
        count = len(nouns)
    i = 0
    list_out = []
    if repeats == True:
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        while i < count:
            list_out.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
            i += 1
    else:
        while i < count:
            list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            i += 1
    return list_out


print(get_jokes_adv(2,False))
print(get_jokes_adv(5,True))
print(get_jokes_adv(7,True))
print(get_jokes_adv(4,()))
