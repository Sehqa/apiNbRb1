import requests
from currency import Currency
from const_for_api import *
from datetime import date
from datetime import timedelta

class NbApi:
    @staticmethod
    def get_currencies():
        list_currencies = []
        request = requests.get(url=ALL_CURRENCIES)
        for i in range(0, len(request.json())):
            currency_object = Currency(request.json()[i])
            list_currencies.append(currency_object)
        return list_currencies

    @staticmethod
    def get_statistics():
        start_date = date.today()-timedelta(days=30)
        end_date =date.today()
        list_statistics = []
        cur = NbApi.get_currencies()
        print(start_date)
        print(end_date)
        for i in range(0, len(cur)):
            req = requests.get(url=CURRENT_DYMANICS + str(
                cur[i].cur_id) + "?startDate=" + str(start_date) + "&endDate=" + str(end_date))
            list_statistics.append(req.json())

        return list_statistics


print(NbApi.get_statistics())