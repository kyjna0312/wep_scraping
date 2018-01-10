from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
nameList = bsObj.findAll({"h1", "h2", "h3", "h4", "h5", "h6"})
print(nameList)
for name in nameList:
    print(name.get_text())
