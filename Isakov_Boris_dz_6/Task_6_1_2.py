from pprint import pprint


def get_parse_attrs(log_line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    ip_index = log_line.index('-')
    remote_addr = log_line[0:ip_index - 1]
    request_start_index = log_line.index('"')
    cut_log_line = log_line[request_start_index + 1:len(log_line)]
    request_last_index = cut_log_line.index(' ')
    request_type = cut_log_line[:request_last_index]
    second_cut_log_line = cut_log_line[request_last_index + 1:len(cut_log_line)]
    resource_last_index = second_cut_log_line.index(' ')
    requested_resource = second_cut_log_line[:resource_last_index]
    parcing_result = (remote_addr, request_type, requested_resource)
    return parcing_result


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    ip_dict = {}  # словарь для записи ip адрессов и количества отправленных запросов с этих адресов
    for line in file_1:
        result=get_parse_attrs(line)
        if str(result[0]) in ip_dict:
            ip_dict.update({str(result[0]):(int(ip_dict.get(str(result[0])))+1)})
        else:
            ip_dict.setdefault(result[0], 1)
        list_out.append(result)
sorted_ip_adresses = sorted(ip_dict.items(), key=lambda i: i[1])  # сортировка пар из словаря по наибольшему из значений

pprint(list_out)
print("Spammer's id adress:")
print(sorted_ip_adresses[-1])
