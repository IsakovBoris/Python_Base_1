import re


def logs_parse(log: str) -> tuple:
    """
    Парсит переданную строку лога на атрибуты и возвращает кортеж
    :param log: строковое входное значение обрабатываемого лога
    :return: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>) | ValueError
    """
    remote_addr = re.compile(r"(^[\w.:]+)")
    request_datetime=re.compile(r"\[([\w/:+\s]+)")
    request_type = re.compile(r"([A-Z]+)\s+/")
    requested_resource = re.compile(r"(/+\w+/+\w+_\d+)")
    response_code = re.compile(r"\"\s+(\d+)\s+\d+")
    response_size = re.compile(r"\d+\s+(\d+)+\s+\"")
    if (remote_addr.findall(log)) and (request_datetime.findall(log)) and (request_type.findall(log)) \
            and (requested_resource.findall(log)) and (response_code.findall(log)) and (response_size.findall(log)):
        result_tuple = (
        (remote_addr.findall(log)[0]), (request_datetime.findall(log)[0]), (request_type.findall(log)[0]),
        (requested_resource.findall(log)[0]), (response_code.findall(log)[0]), (response_size.findall(log)[0]))
    else:
        err_msg = f'wrong log: {log}'
        raise ValueError(err_msg)
    return result_tuple


if __name__ == '__main__':
    with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
        for line in file_1:
            print(logs_parse(line))
