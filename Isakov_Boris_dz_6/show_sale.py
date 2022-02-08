import sys
command_line=sys.argv
i=0
counter=0
if len(command_line) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as file_1:
            for line in file_1:
                print(line.strip())
if len(command_line) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as file_1:
        for i,line in enumerate(file_1):
            counter += 1
            if i in range(int(command_line[1]) - 1, i + 1):
                print(line.strip())
        if counter < int(command_line[1]):
            print('Нет данных о продаже №',command_line[1])
if len(command_line) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as file_1:
        for i,line in enumerate(file_1):
            counter += 1
            if i in range (int(command_line[1])-1, int(command_line[2])):
                print(line.strip())
        if counter < int(command_line[2]):
            print('Нет данных о продаже №',command_line[2])
