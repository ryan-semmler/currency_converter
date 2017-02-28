import currency

def test_currency():
    assert Currency.currency('$40') == ('USD', 40)
    assert Currency.currency('€150') == ('EUR', 150)
    assert Currency.currency('¥1000') == ('JPY', 1000)
    assert Currency.currency(40, 'USD') == ('USD', 40)
    assert Currency.currency(150, 'EUR') == ('EUR', 150)
    assert Currency.currency(1000, 'JPY') == ('JPY', 1000)

def test_eq():
    assert Currency.__eq__(('USD', 40), ('USD', 40)) == True
    assert Currency.__eq__(('USD', 40), ('USD', 41)) == False
    assert Currency.__eq__(('EUR', 40), ('USD', 40)) == False

def test_add():
    assert Currency.__add__(('USD', 40), ('USD', 41)) == ('USD', 81)
    assert Currency.__add__(('USD', 40), ('JPY', 41)) == DifferentCurrencyCodeError

def test_sub():
    assert Currency.__sub__(('USD', 40), ('USD', 39)) == ('USD', 1))
    assert Currency.__sub__(('USD', 40), ('JPY', 39)) == DifferentCurrencyCodeError

def test_mul():
    assert Currency.__mul__(('USD', 40), 5) == ('USD', 200)
