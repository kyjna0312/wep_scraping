# 2013250012 김용진
# 2018 - 01 - 12
# 해당 요일에 해당하는 네이버 인기검색어를 크롤링하는 python 프로그램

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://datalab.naver.com/keyword/realtimeList.naver?where=main")
bsObj = BeautifulSoup(html, "html.parser")

span = bsObj.findAll("div", {"class" : "keyword_rank"})
for text in span:
    print(text.get_text())
