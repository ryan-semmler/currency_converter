import currency

def converter_test():
    assert currency_converter.convert(Currency(1000, 'USD'), 'EUR') == (740.0, 'EUR')
    assert currency_converter.convert(Currency(1, 'USD'), 'USD') == (1, 'USD')
    assert currency_converter.convert(Currency(50, 'USD'), 'GBP') == UnknownCurrencyCodeError
    assert currency_converter.convert(Currency(100, 'EUR'), 'JPY') == (16216.216216216217, 'JPY')
