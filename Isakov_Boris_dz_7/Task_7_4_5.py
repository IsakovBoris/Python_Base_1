import os
import json


def files_size_counter(base_dir):
    dict_out={}
    for root, dirs, files in os.walk(base_dir):
        file_list=(files)
        for file in file_list:
            name=os.path.splitext(file)
            if name[1]:
                type=name[1][1:len(name[1])]
                size=os.stat(os.path.join(root, file)).st_size
                bytes_level = str(size // 10)
                upper_bound = 10 ** len(bytes_level)
                key=upper_bound
                value=1
                if dict_out.get(key):
                    types_list = dict_out.get(key)[1]
                    types_list.append(type)
                    new_value = dict_out.get(key)[0] + 1
                    upd_dict={key:(new_value,types_list)}
                    dict_out.update(upd_dict)
                else:
                    dict_out.setdefault(key, (value,[type]))
    sorted_dict=sorted(dict_out.items(), key=lambda element: element[0])
    return dict(sorted_dict)


if __name__ == "__main__":
    BASE_DIR = '/Users/Boris/Documents/Code/Python_Base_1-/Isakov_Boris_dz_7/some_data'
    result=files_size_counter(BASE_DIR)
    print(result)
    with open('some_data_summary.json', 'w', encoding='utf-8') as fw:
        json.dump(result, fw, ensure_ascii=False, indent=2)
