import requests
from datetime import datetime, date
from Task_4_2 import currency_rates

def currency_rates_adv(code: str):
    """возвращает курс валюты и дату запроса `code` по отношению к рублю"""
    response = requests.api.get("http://www.cbr.ru/scripts/XML_daily.asp")
    values_to_search = str(response.text)
    date_value=values_to_search.find('Date')
    date_str=values_to_search[date_value+6:date_value+16]
    date_time_obj=datetime.strptime(date_str, "%d.%m.%Y")
    date_time_obj=date_time_obj.date()
    result_value = currency_rates(code)
    return (result_value, date_time_obj)


currency, date_value = currency_rates_adv("gbp")

empty = bool(not currency and not date_value)
if not empty and not isinstance(currency, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance (date_value, date):
    raise TypeError("Неверный тип данных у даты")
print(currency, date_value)

