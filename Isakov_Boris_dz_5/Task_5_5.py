def get_uniq_numbers(src: list):
    unique_numbers = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unique_numbers.add(el)
        else:
            unique_numbers.discard(el)
        tmp.add(el)
    unique_nums_ord = [el for el in src if el in unique_numbers]
    return unique_nums_ord


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))
