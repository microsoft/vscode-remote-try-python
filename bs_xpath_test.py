from bs4 import BeautifulSoup
from lxml import etree
import requests
  
  
url = "https://www.remax.com/mi/kalamazoo/home-details/3536-rollridge-ave-kalamazoo-mi-49004/10516505409216359515/M00000329/21022607"
  
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
  
webpage = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))
prices = dom.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "h3", " " ))]/text()')[1]
prices = prices.replace(",", "")
prices = prices.replace("$", "")
prices = prices.replace(" ", "")

print(prices)

