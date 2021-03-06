from urllib.request import urlopen
import json

mode = 'ur'
if mode == 'url':
    currency={
    "base": "EUR",
    "date": "2017-05-19",
    "rates": {
        "AUD": 1.5031,
        "BGN": 1.9558,
        "BRL": 3.7227,
        "CAD": 1.5169,
        "CHF": 1.0921,
        "CNY": 7.7015,
        "CZK": 26.503,
        "DKK": 7.4411,
        "GBP": 0.85908,
        "HKD": 8.6999,
        "HRK": 7.439,
        "HUF": 309.6,
        "IDR": 14881,
        "ILS": 4.0087,
        "INR": 72.202,
        "JPY": 124.35,
        "KRW": 1251.5,
        "MXN": 20.938,
        "MYR": 4.831,
        "NOK": 9.3923,
        "NZD": 1.6227,
        "PHP": 55.564,
        "PLN": 4.2005,
        "RON": 4.5602,
        "RUB": 63.781,
        "SEK": 9.7893,
        "SGD": 1.5509,
        "THB": 38.422,
        "TRY": 4.0275,
        "USD": 1.1179,
        "ZAR": 14.827
        }
    }
else:

    currency = json.loads(urlopen('http://api.fixer.io/latest').read().decode())

rates = currency['rates']
print(currency['date'])
for k, v in rates.items():
    print('Za 100 {} Kupisz: {} {}'.format(currency['base'], v*100, k))