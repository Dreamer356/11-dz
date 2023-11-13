import requests
from bs4 import BeautifulSoup
from forex_python.converter import CurrencyRates


class CurrencyConverter:
    def __init__(self):
        self.c = CurrencyRates()

    def convert_to_usd(self, amount, from_currency):
        rate = self.c.get_rate(from_currency, 'USD')
        converted_amount = amount * rate
        return converted_amount


def get_usd_exchange_rate():
    url = 'https://www.bank.gov.ua/control/uk/curmetal/detail/currency?period=daily'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    usd_rate = soup.find('td', {'class': 'cell_c1'}).text
    return float(usd_rate.replace(',', '.'))


if __name__ == "__main__":
    usd_exchange_rate = get_usd_exchange_rate()
    print(f'Курс долара США: {usd_exchange_rate}')
    converter = CurrencyConverter()
    amount = float(input('Введіть кількість валюти вашої країни: '))
    usd_amount = converter.convert_to_usd(amount, 'UAH')

    # Виведення результату
    print(f'{amount} валюти вашої країни дорівнює {usd_amount:.2f} доларам США.')