import requests
from prettytable import PrettyTable

class CryptoPriceMonitor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    def get_all_prices(self):
        parameters = {
            'start': '1',
            'limit': '100',  # Adjust the limit as needed
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
        }
        response = requests.get(self.url, headers=headers, params=parameters)
        data = response.json()
        return data['data']

    def print_prices_table(self):
        all_prices = self.get_all_prices()
        table = PrettyTable()
        table.field_names = ["Symbol", "Name", "Price (USD)"]

        for crypto in all_prices:
            symbol = crypto['symbol']
            name = crypto['name']
            price = crypto['quote']['USD']['price']
            table.add_row([symbol, name, price])

        print(table)

# Replace with your CoinMarketCap API key
api_key = 'c9ceaa19-545d-4c60-8c59-862eef87115e'

# Create an instance of the CryptoPriceMonitor
monitor = CryptoPriceMonitor(api_key)
# Print all prices in a table
monitor.print_prices_table()
