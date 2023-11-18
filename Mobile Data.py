
mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchange_rate': 110.45
            }

# convert price
def convert_to_bdt(price_usd):
    price_usd_float = float(price_usd.replace('USD', ''))
    price_bdt = price_usd_float * mobile_data['exchange_rate']
    return price_bdt

# print all dictonaries
for mobile in mobile_data['data']:
    bdt = convert_to_bdt(mobile['price'])

    print(f"{mobile['name']} made in {mobile['made']}. The price is {mobile['price']} USD, which is almost equal to {bdt} BDT")
