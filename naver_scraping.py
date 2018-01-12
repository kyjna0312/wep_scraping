# 2013250012 김용진
# 2018 - 01 - 12
# 해당 요일에 해당하는 네이버 인기검색어를 크롤링하는 python 프로그램

from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import *

html = urlopen("https://datalab.naver.com/keyword/realtimeList.naver?where=main")
bsObj = BeautifulSoup(html, "html.parser")

span = bsObj.findAll("div", {"class" : "select_date"})

for word in span:
    naver = word.get_text()

root = Tk()
root.title("인기 검색어")

text = Label(root, text=naver).pack()

root.mainloop()
