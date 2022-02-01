import requests
from datetime import datetime

def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    code = code.upper()
    try:
        response = requests.api.get("http://www.cbr.ru/scripts/XML_daily.asp")
        values_to_search = str(response.text)

        currency_indx_search = values_to_search.index(code)
        currency_search = values_to_search[currency_indx_search:len(values_to_search)]

        denomination_indx_search = currency_search.index('Nominal')
        denomination_search = currency_search[denomination_indx_search + 8:]
        denomination_indx_end = denomination_search.index('Nominal')
        denomination = denomination_search[:denomination_indx_end - 2]

        value_indx_search = currency_search.index('Value')
        value_search = currency_search[value_indx_search + 6:]
        value_last_indx_search = value_search.index('Value')
        value = value_search[:value_last_indx_search - 2]
        result_value = float(value.replace(',', '.'))
        if int(denomination) > 1:
            result_value = result_value / (int(denomination))
        return result_value
    except ValueError:
        pass


def currency_rates_adv(code: str):
    """возвращает курс валюты и дату запроса `code` по отношению к рублю"""
    response = requests.api.get("http://www.cbr.ru/scripts/XML_daily.asp")
    values_to_search = str(response.text)
    date_value=values_to_search.find('Date')
    date_str=values_to_search[date_value+6:date_value+16]
    date_time_obj=datetime.strptime(date_str, "%d.%m.%Y")
    date_time_obj=date_time_obj.date()
    result_value = currency_rates(code)
    return (f'{result_value}, {date_time_obj}')
