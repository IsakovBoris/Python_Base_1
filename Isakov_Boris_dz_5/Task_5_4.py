def get_numbers(src: list):
    larger_numbers = set()
    for i in range(len(src) - 1):
        if src[i] < src[i + 1]:
            larger_numbers.add(src[i + 1])
    larger_nums_ord = [el for el in src if el in larger_numbers]
    return larger_nums_ord


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))
