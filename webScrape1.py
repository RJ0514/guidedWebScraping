# Guided Web Scraping

from bs4 import BeautifulSoup
import re
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents


'''
with open("index2.html","r") as f:
    doc = BeautifulSoup(f, "html.parser")


tags = doc.find_all(text=re.compile("\$.*"))

for tag in tags:
    print(tag.strip())
'''

prices = {}
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    coin_name = name.p.string
    coin_price = price.span.string

    prices[coin_name] = coin_price

for p in prices:
    print('Coin Name: ', p, '\tCoin Price: ',prices[p])
    print()
