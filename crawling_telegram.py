# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import time
import requests
import telegram

bot = telegram.Bot(token='485029394:AAEMIt1L0HkolhN-wpQ8aWLJh3J7zT-sNFk')
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# url = "http://finance.naver.com/sise/sise_low_up.nhn"
# html = requests.get(url).text
# soup = BeautifulSoup(html, 'html.parser')
# table = soup.find("table",{"class":"type_2"})
# aa =  table.find_all("a")
# list = []
# for name in aa:
#     # print(name.text)
#     list.append(name.text)
while True:
    req = requests.get('http://finance.naver.com/item/board_read.nhn?code=007460&nid=78742140')
    req.encoding = 'utf-8'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all("em",{"class": "no_down"})
    print(posts)
    latest = posts[1].text

    # with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
    #     before = f_read.readline()
    #     if before != latest:
    #         # for x in range(len(list)):
    #         bot.sendMessage(chat_id=chat_id, text="새글 올라옴")
    #     else:
    #         bot.sendMessage(chat_id=chat_id, text="새글 안올라옴")
    #     f_read.close()
    #
    # with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
    #     f_write.write(latest)
    #     f_write.close()
    #
    # time.sleep(60) # 60초(1분)을 쉬어줍니다.