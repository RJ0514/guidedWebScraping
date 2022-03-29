from bs4 import BeautifulSoup
import re
import requests

product = input("What product do you want to searach for? ")

url = f"https://www.newegg.ca/p/pl?d={product}&N=4131"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_ = "list-tool-pagination-text")
pages = int(str(page_text).split("/")[-3].split(">")[-1][:-1])


items_found = {}
for page in range (1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={product}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    div = doc.find(class_ = "item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
    items = div.find_all(text = re.compile(product))                        

    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue
        
        link = parent['href']
        next_parent = item.find_parent(class_="item-container")\
        
        try:
            price = next_parent.find(class_="price-current").strong.string
            items_found[item] = {"price" : int(price.replace(",","")) , "link" : link}
        except:
            pass

results = sorted(items_found.items(), key = lambda x: x[1]['price'] )

indexCount = 0;
for item in results:
    indexCount+=1
    print(indexCount," ",item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print()