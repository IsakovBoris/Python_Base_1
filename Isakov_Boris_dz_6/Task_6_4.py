import sys


def prepare_str(path_users_file: str, path_hobby_file: str) -> str:
    with open(path_users_file, 'r', encoding='utf-8') as file_1, open(path_hobby_file, 'r',
                                                                  encoding='utf-8') as file_2:
        result_str = (f'{file_1.readline().strip()}: {file_2.readline().strip()}')
        counter_users=0
        for line_2 in file_2:
            result_str = (f'{result_str}\n{file_1.readline().strip()}: {line_2.strip()}')
        for line in file_1:
            result_str = (f'{result_str}\n{line.strip()}: {None}')
            counter_users +=1
        if counter_users == 0:
            sys.exit(1)
    return result_str.replace(',',' ')


string_to_record = prepare_str('users.csv', 'hobby.csv')
with open('users_hobby.txt', 'a', encoding='utf-8') as file_3:
    file_3.write(string_to_record)
