from util.moneyOperations import *

def start():
    valute = 'Выберите ID валюты \n'
    for i in range(len(currencies)):
        valute += ('ID: {0} Валюта:{1}\n'.format(i, currencies[i]))
    print(valute)
    id_curr = int(input())
    print('Введите число:')
    value = float(input())
    convert(currencies[id_curr], value)
