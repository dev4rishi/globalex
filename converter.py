from forex_python.converter import CurrencyRates
c=CurrencyRates()

def convert(base_cur,final_cur,amt):
    return c.convert(base_cur,final_cur,amt)
print(convert('USD','EUR',80))