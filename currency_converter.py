from currency import Currency
rates = {'USD': 1.0, 'EUR': 0.74, 'JPY': 120.0}


class UnknownCurrencyCodeError(Exception):
    pass


class CurrencyConverter:

    def __init__(self, code, amount, symbol):
        self.code = code
        self.amount = amount
        self.symbol = symbol


    # def is_same_type(self, other):
    #     if self.code == other.code:
    #         return True
    #     else:
    #         return False
    #
    # def sym_to_code(self):
    #     if self.symbol == '$':
    #         code = 'USD'
    #     elif self.symbol == '€':
    #         code = 'EUR'
    #     elif self.symbol == '¥':
    #         code = "JPY"
    #     else:
    #         return ValueError

    def convert(self, convert_to):
        if self.code in rates and convert_to in rates:
            return (rates[convert_to] * self.amount / rates[self.code], convert_to)
        else:
            raise Exception(UnknownCurrencyCodeError)


print(CurrencyConverter.convert(Currency(100, 'EUR'), 'JPY'))
