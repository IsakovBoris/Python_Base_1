import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    dict_users_hobby = {}
    with open(path_users_file, 'r',encoding='utf-8-sig') as file_1:  # без sig при чтении к первой строке добавляется разделитель '\ufefftest'
        names = file_1.read()
        users = names.splitlines()
    with open(path_hobby_file, 'r', encoding='utf-8-sig') as file_2:
        interests = file_2.read()
        hobby = interests.splitlines()

    i = 0
    j = 0
    while i < len(users):
        if len(users) > len(hobby):
            if j < len(hobby):
                dict_users_hobby.setdefault(users[i].replace(',',' '), hobby[j].replace(',',', '))
            else:
                dict_users_hobby.setdefault(users[i], None)
        else:
            sys.exit(1)
        i += 1
        j += 1

    return dict_users_hobby


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)

print(dict_out)
