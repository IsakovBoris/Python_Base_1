import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r"([A-Za-z0-9-_.]+)@+([A-Za-z0-9-_]+\.[A-Za-z0-9-_]+)")
    if RE_MAIL.findall(email):
        dict_out=dict(username=RE_MAIL.findall(email)[0][0],domain=RE_MAIL.findall(email)[0][1])
    else:
        err_msg = f'wrong email: {email}'
        raise ValueError(err_msg)
    return dict_out


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
