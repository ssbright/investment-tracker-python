import requests



r = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=Bitcoin&vs_currencies=USD')
response = r.json()
coin = response['bitcoin']
value = coin['usd']

print(value)