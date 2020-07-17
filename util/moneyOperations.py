import requests
import json

currencies = ['USD', 'EUR', 'CAD']


def get_course(currency):
    global_request = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    global_data = json.loads(global_request.text)['Valute']
    return global_data[currency]['Value']


def convert(currencies, value):
    print('Результат: {0}'.format(float(value / float(get_course(currencies)))))
