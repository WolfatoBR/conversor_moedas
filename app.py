from engine.clients import CoinConversorServices

client = CoinConversorServices()
conversion = client.converter('USD','BRL')

print(conversion)