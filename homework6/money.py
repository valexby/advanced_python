import requests


API_KEY = '4517c1b02e0d131860a07e86b7c73874'


class Money:
    def __init__(self, number, currency='USD'):
        if currency not in Money.list_currencies():
            raise ValueError("Unsupported currency - \"{}\"".format(currency))
        self.number = number
        self.currency = currency

    def convert(self, new_currency):
        if new_currency == self.currency:
            return self.number
        response = requests.get(
            'http://apilayer.net/api/live',
            params={'access_key': API_KEY}).json()
        usd = self.number / response['quotes']['USD{}'.format(self.currency)]
        quote = response['quotes'].get("USD{}".format(new_currency))
        if quote is None:
            message = "Unsupported currency - \"{}\"".format(new_currency)
            raise ValueError(message)
        return usd * quote

    def __radd__(self, other):
        if other == 0:
            return Money(self.number, self.currency)
        converted = other.convert(self.currency)
        return Money(converted + self.number, currency=self.currency)

    def __add__(self, other):
        converted = other.convert(self.currency)
        return Money(converted + self.number, currency=self.currency)

    def __mul__(self, other):
        return Money(self.number * other, currency=self.currency)

    def __rmul__(self, other):
        return Money(self.number * other, currency=self.currency)

    def __str__(self):
        return "{} {}".format(self.number, self.currency)

    @staticmethod
    def list_currencies():
        response = requests.get('http://apilayer.net/api/list',
                                params={'access_key': API_KEY})
        return list(response.json()['currencies'].keys())
