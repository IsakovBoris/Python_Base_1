import os


def creation_file(path,name):
    if not os.path.exists(path):
        if name.endswith('.py') or name.endswith('.html'):
            file_name = name
            file = open(file_name, 'w')
            file.close()
            os.replace(file_name, path)
        else:
            os.makedirs(path)


def create_project(base_dir,config):
    head_folder_path = ()
    main_folder_path=()
    folder_path=()
    middle_folder_path=()
    for line in config:
        if line[0] != '|':
            head_folder_name = line
            head_folder_path = os.path.join(base_dir, head_folder_name)
            creation_file(head_folder_path,head_folder_name)
        if line[0] == '|'and line[1] != '|':
            main_folder_name=line[1:len(line)]
            main_folder_path = os.path.join(head_folder_path, main_folder_name)
            creation_file(main_folder_path, main_folder_name)
        if line[1] == '|' and line[2] != '|':
            folder_name = line[2:len(line)]
            folder_path = os.path.join(main_folder_path, folder_name)
            creation_file(folder_path,folder_name)
        if line[2] == '|'and line[3] !='|':
            middle_folder_name=line[3:len(line)]
            middle_folder_path = os.path.join(folder_path, middle_folder_name)
            creation_file(middle_folder_path,middle_folder_name)
        if line[3] == '|'and line[4] !='|':
            lower_folder_name = line[4:len(line)]
            lower_folder_path = os.path.join(middle_folder_path, lower_folder_name)
            creation_file(lower_folder_path,lower_folder_name)


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    with open('config.yaml', 'r', encoding='utf-8') as file:
        configuration = file.read().splitlines()
    create_project(BASE_DIR,configuration)
