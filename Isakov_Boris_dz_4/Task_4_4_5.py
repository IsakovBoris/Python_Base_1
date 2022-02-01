import sys
from utils import currency_rates_adv

try:
    value = (sys.argv[1])
    print(currency_rates_adv(value))
except IndexError:
    pass

"""
Комментарий с содержанием результатов вывода модуля через терминал:
MacBook-Pro-Isakov:Isakov_Boris_dz_4 Boris$ python3 Task_4_4_5.py
MacBook-Pro-Isakov:Isakov_Boris_dz_4 Boris$ python3 Task_4_4_5.py AMD
0.160394, 2022-02-01
MacBook-Pro-Isakov:Isakov_Boris_dz_4 Boris$ python3 Task_4_4_5.py HDK
None, 2022-02-01
MacBook-Pro-Isakov:Isakov_Boris_dz_4 Boris$ python3 Task_4_4_5.py Usd
77.4702, 2022-02-01
MacBook-Pro-Isakov:Isakov_Boris_dz_4 Boris$ 
"""