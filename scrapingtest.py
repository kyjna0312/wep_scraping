from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org/"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-bodyContent-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing somthing! No worries thought!")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("---------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")
