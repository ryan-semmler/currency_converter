class DifferentCurrencyCodeError(Exception):
        pass


class Currency:

    def __init__(self, amount, code=''):
        self.code = code
        self.amount = amount

    def currency(self, code=''):
        if not code:
            if self[0] == '$':
                code = 'USD'
            elif self[0] == '¥':
                code = 'JPY'
            elif self[0] == '€':
                code = 'EUR'
            amount = int(self[1:])
            return (code, amount)
        return (code, self)

    def __eq__(self, other):
        return self.code == other.code and self.amount == other.amount

    def __add__(self, other):
        if self.code == other.code:
            return (self.amount + other.amount, self.code)
        raise Exception(DifferentCurrencyCodeError)

    def __sub__(self, other):
        if self.code == other.code:
            return (self.amount - other.amount, self.code)
        raise Exception('DifferentCurrencyCodeError')

    def __mul__(self, multiplier):
        return (self.code, self.amount * multiplier)
