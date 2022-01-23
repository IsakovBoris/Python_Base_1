expression_a = 15 * 3
print(f'Результат выражения 15*3 = {expression_a},тип результата: {type(expression_a)}')
expression_b = 15 / 3
if isinstance(expression_b,float):
    print(f'Результат выражения 15/3 = {expression_b},тип результата: сlass float' )
expression_c = 15 // 2
if isinstance(expression_c,int):
    print(f'Результат выражения 15//2 = {expression_c},тип результата: сlass int')
expression_d = 15 ** 2
print(f'Результат выражения 15**2 = {expression_d},тип результата: {type(expression_d)}')