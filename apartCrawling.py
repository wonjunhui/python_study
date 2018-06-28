from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
# import telegram
import os
import time

url = "http://finance.naver.com/sise/sise_low_up.nhn"
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
table = soup.find("table",{"class":"type_2"})
aa =  table.find_all("a")
list = []
for name in aa:
	# print(name.text)
	list.append(name.text)
	print(name.text)
# print(list)
# bot = telegram.Bot(token='485029394:AAEMIt1L0HkolhN-wpQ8aWLJh3J7zT-sNFk')
# chat_id = bot.getUpdates()[-1].message.chat.id
# bot.sendMessage(chat_id=chat_id, text=list)


# print(test)
# td = table.find_all("td")
# aa = td.find("a",{"class":"title"})
# print(table)
# print(aa)
# divs = soup.findAll("table", {"class": "an"})  

# print(title)
# titleData = soup.find_all("td",{"a",{"class":{"title"}}})
# my_titles = soup.select(
#     'tr > td'
#     )

# print(soup.prettify())
# print(soup.find_all('a'))
# for link in soup.find_all('a'): 
	# print(link.get_text())


# my_titles는 list 객체
# for title in my_titles:
#     # Tag안의 텍스트
#     print(title.text)
#     # Tag의 속성을 가져오기(ex: href속성)
#     print(title.get('href'))
#contentarea > div.box_type_l > table > tbody > tr:nth-child(3) > td:nth-child(3)