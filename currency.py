# currency.py
import urllib.request

class Currency:
    VALID_CODES = ['USD', 'EUR', 'SEK', 'CAD', 'CNY', 'GBP']

    def __init__(self, amount=0.0, currency_code='USD'):
        if isinstance(amount, (int, float)) and currency_code in self.VALID_CODES:
            self.amount = float(amount)
            self.code = currency_code
        else:
            self.amount = 0.0
            self.code = ''

    def __str__(self):
        return f"{self.amount:.2f} {self.code}"

    def __repr__(self):
        return f"Currency({self.amount}, '{self.code}')"

    def convert_to(self, new_code):
        if self.code == new_code:
            return Currency(self.amount, self.code)
        url = f"https://www.google.com/finance/converter?a={self.amount}&from={self.code}&to={new_code}"
        try:
            web_obj = urllib.request.urlopen(url)
            result_str = str(web_obj.read())
            web_obj.close()
            index = result_str.find('class=bld>')
            start = index + 10
            end = result_str.find('</span>', start)
            value = result_str[start:end].split()[0]
            converted_amount = float(value)
            return Currency(converted_amount, new_code)
        except Exception as e:
            print("Error during conversion:", e)
            return Currency(0, new_code)

    def __add__(self, other):
        if isinstance(other, Currency):
            other_converted = other.convert_to(self.code)
            return Currency(self.amount + other_converted.amount, self.code)
        elif isinstance(other, (int, float)):
            return Currency(self.amount + other, self.code)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Currency):
            other_converted = other.convert_to(self.code)
            return Currency(self.amount - other_converted.amount, self.code)
        elif isinstance(other, (int, float)):
            return Currency(self.amount - other, self.code)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Currency(other - self.amount, self.code)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Currency):
            other_converted = other.convert_to(self.code)
            return self.amount > other_converted.amount
        return NotImplemented
