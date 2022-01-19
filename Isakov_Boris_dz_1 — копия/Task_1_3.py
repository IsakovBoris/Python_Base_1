def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if number>=11 and number<=14:
        percentage='процентов' #percentage - переменная отвечающая за слово в правильном склонении
    else:
        units_check = number % 10 #units_check -переменная для проверки единиц на конце подставляемых числел numbers
        if units_check == 1:
            percentage='процент'
        elif units_check ==2 or units_check==3 or units_check==4:
            percentage='процента'
        else:
            percentage='процентов'
    result=(f' {number} {percentage}')
    return result

for i in range(1,101):
    print(transform_string(i))