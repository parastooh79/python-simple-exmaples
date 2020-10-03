import requests
result = requests.get('https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD')

bit_price = result.json()

print('The highest price is %s'  %bit_price['high'])
print('----------------------------------------')
print('The minimum price is %s'  %bit_price['low'])