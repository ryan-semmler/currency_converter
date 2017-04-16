from currency import Currency, DifferentCurrencyCodeError

def test_currency():
    assert Currency.currency('$40') == ('USD', 40)
    assert Currency.currency('€150') == ('EUR', 150)
    assert Currency.currency('¥1000') == ('JPY', 1000)
    assert Currency.currency(40, 'USD') == ('USD', 40)
    assert Currency.currency(150, 'EUR') == ('EUR', 150)
    assert Currency.currency(1000, 'JPY') == ('JPY', 1000)

def test_eq():
    assert Currency(40, 'USD') == Currency(40, 'USD')
    assert Currency(40, 'USD') != Currency(41, 'USD')
    assert Currency(40, 'EUR') != Currency(40, 'USD')

def test_add():
    assert Currency(40, 'USD') + Currency(41, 'USD') == Currency(81, 'USD')
    assert Currency(40, 'USD') + Currency(41, 'JPY') == DifferentCurrencyCodeError

def test_sub():
    assert Currency(40, 'USD') - Currency(39, 'USD') == Currency(1, 'USD')
    assert Currency(40, 'USD') - Currency(39, 'JPY') == DifferentCurrencyCodeError

def test_mul():
    assert Currency(40, 'USD') * 5 == Currency(200, 'USD')
