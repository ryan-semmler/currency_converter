from currency import *


class CurrencyConverter:

    def __init__(self, cur_object, new_code):
        self.currency = cur_object
        self.code = new_code
        self.rates = {'USD': 1.0, 'EUR': 0.74, 'JPY': 120}

    def convert(self, cur_object, new_code):
        if new_code in '$¥€' or new_code in ['USD', 'JPY', 'EUR']:
            if new_code == '$':
                new_code = 'USD'
            elif new_code == '¥':
                new_code = 'JPY'
            elif new_code == '€':
                new_code = 'EUR'
            else:
                raise Exception(UnknownCurrencyCodeError)
        return Currency(cur_object.amount * self.rates[cur_object.code], new_code)
