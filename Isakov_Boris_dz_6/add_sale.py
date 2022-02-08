import sys
value= (sys.argv[1])
bakery_sales=f'''{value}
'''
with open('bakery.csv', 'a', encoding='utf-8') as file:
   file.write(bakery_sales)
