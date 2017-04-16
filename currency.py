class DifferentCurrencyCodeError(Exception):
        pass


class UnknownCurrencyCodeError(Exception):
    pass


class Currency:

    def __init__(self, amount, code=''):
        if code == '$':
            code = 'USD'
        elif code == '¥':
            code = 'JPY'
        elif code == '€':
            code = 'EUR'
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
            return Currency(amount, code=code)
        return Currency(self[1:], code=code)

    def __eq__(self, other):
        return self.code == other.code and self.amount == other.amount

    def __add__(self, other):
        if self.code == other.code:
            return Currency(self.amount + other.amount, code=self.code)
        raise Exception(DifferentCurrencyCodeError)

    def __sub__(self, other):
        if self.code == other.code:
            return Currency(self.amount - other.amount, code=self.code)
        raise Exception(DifferentCurrencyCodeError)

    def __mul__(self, multiplier):
        return Currency(self.amount * multiplier, code=self.code)

    def __str__(self):
        return '{} {}'.format(self.amount, self.code)

    def __repr__(self):
        return '{} {}'.format(self.amount, self.code)
