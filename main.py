import datetime

import requests
from currency import Currency
from datetime import date
from datetime import timedelta
url='https://www.nbrb.by/api/exrates/currencies'

req = requests.get(url=url)

#print(req.json()[0])

cur = Currency(req.json()[0])

print(req.json()[0])
# Мне впадлу перебирать все значения полей так что будет магия
print(cur.__dict__.values())
#данные в обьекте и json совпадают + кайф



