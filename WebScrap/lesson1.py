python
import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.ksl.com/auto/")
r = requests.get("http://www.ksl.com/auto/search?cx_navSource=hp_listings&page=0")
r.content

soup = BeautifulSoup(r.content)
print soup.prettify()


#for x in soup.find_all('p'):
#...     print(x.text)

for div in soup.find_all('div',class_="listing"):
     print(div.text)
