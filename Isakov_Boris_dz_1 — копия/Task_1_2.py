def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    index_list = 0 #индекс для перебора элементов списка
    unit_total = 0 #переменная, в которую записывается сумма цифр, проверяемого числа
    final_result = 0 #переменная, для сложения элементов списка, удовлетворяющих условию задания
    while index_list < len(dataset): #цикл проверки элементов списка
        number_check = dataset[index_list] #переменная, которой присвается значение элемента для проверки условия суммы цифр
        while number_check > 0: #цикл разбития числа на цифры и подсчет суммы этих цифр
            unit_number = number_check % 10
            unit_total = unit_total + unit_number
            number_check = number_check // 10
        if unit_total % 7 == 0: #условие, при котором элемент из списка записывается для итогового сложения
            final_result = final_result + dataset[index_list]
        unit_total = 0 #обнуление переменной суммы цифр для избежания дублирования
        index_list += 1
    return final_result

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
    сумма цифр которых делится нацело на 7 (с объявлением двух дополнительных списков для записи измененных элементов"""
    dataset_list_17 = [] #список в который помещаются элементы из заданного списка с прибавлением 17 к каждому элементу
    index_list_17 = 0 #индекс для перебора нового списка
    final_list = [] #итоговый список в который записываются элементы соответсвующие условию задачи
    index_list = 0
    unit_total = 0
    final_result = 0 #переменная, для сложения элементов списка, удовлетворяющих условию задания из цикла final_list
    index_result = 0 #индекс для перебора элементов из цикла final_list
    while index_list_17 < len(dataset): #цикл для записи элементов увеличенных на 17 в новый список
        dataset_list_17.append(dataset[index_list_17] + 17)
        index_list_17 += 1
    while index_list < len(dataset_list_17): #цикл разбития числа на цифры и подсчет суммы этих цифр
        number_check = dataset_list_17[index_list]
        while number_check > 0:
            unit_number = number_check % 10
            unit_total = unit_total + unit_number
            number_check = number_check // 10
        if unit_total % 7 == 0: #условие, при котором элемент из списка записывается в итоговый список
            final_list.append(dataset_list_17[index_list])
        unit_total = 0
        index_list += 1
    while index_result < len(final_list): #цикл для подсчитывания суммы элементов итогового списка
        final_numbers = final_list[index_result]
        final_result = final_result + final_numbers
        index_result += 1
    return final_result

def sum_list_3(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
            сумма цифр которых делится нацело на 7 (без объявления дополнительных списков)"""
    index_list = 0
    unit_total = 0
    final_result = 0
    while index_list < len(my_list): #цикл проверки элементов списка
        number_check = dataset[index_list] + 17 #вместо создания дополнительного списка записываем в переменную, объявленнную для проверки суммы цифр, элемент увеличенный на 17
        while number_check > 0:
            unit_number = number_check % 10
            unit_total = unit_total + unit_number
            number_check = number_check // 10
        if unit_total % 7 == 0:
            final_result = final_result + (dataset[index_list] + 17) #также, подходящий условию задачи элемент из списка увеличиваем на 17 и записываем в итоговое значение
        unit_total = 0
        index_list += 1
    return final_result


my_list =[]
for i in range(1,1001,2):
    my_list.append(i**3)

result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
result_3 = sum_list_3(my_list)
print(result_3)