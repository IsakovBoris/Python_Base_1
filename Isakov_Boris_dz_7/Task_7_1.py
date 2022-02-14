import os


def rename_folder(head_folder,folder_name):
    new_name = input('Введите новое название папки: ')
    change_folder_name = os.path.join(head_folder, new_name)
    return os.rename(folder_name, change_folder_name)


def change_new_folder_name(head_folder,new_folder_name):
    rename_command = os.path.join(head_folder, new_folder_name)
    return os.makedirs(rename_command)


def exist_check(head_folder, path_folder):
    if os.path.exists(path_folder):
        print(f'Папка {path_folder} существует!')
        rename_question = input(f'Переименовать существующую папку {path_folder} Y/N? ')
        if rename_question == 'Y':
            rename_folder(head_folder,path_folder)
        else:
            print(f'Необходимо задать имя, отличное от существующих папок: {os.listdir(head_folder)}')
            new_question = input(f'Переименовать новую папку {path_folder} Y/N? ')
            if new_question == 'Y':
                folder_name = input('Введите новое название папки: ')
                change_new_folder_name(head_folder, folder_name)
            else:
                print(f'Папка {path_folder} осталась без изменений')
    else:
        os.makedirs(path_folder)


def create_folders(base_dir,folders_names):
    for main_folder, folders in folders_names.items():
        main_folder_path = os.path.join(base_dir, main_folder)
        if not os.path.exists(main_folder_path):
            os.mkdir(main_folder_path)
        for folder in folders:
            folder_path = os.path.join(main_folder_path, folder)
            exist_check(main_folder_path, folder_path)

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    folders_in_project = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
    create_folders(BASE_DIR,folders_in_project)
