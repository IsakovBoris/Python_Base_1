import os
import shutil


def tempaltes_replace(base_dir):
    for root, dirs, files in os.walk(base_dir):
        if dirs == ['templates']:
            previous_path = os.path.join(root, 'templates')
            new_path = os.path.join(base_dir, 'templates')
            shutil.copytree(previous_path, new_path, dirs_exist_ok=True)

if __name__ == "__main__":
    BASE_DIR = '/Users/Boris/Documents/Code/Python_Base_1-/Isakov_Boris_dz_7/my_project'
    tempaltes_replace(BASE_DIR)
