# -*- coding: utf-8 -*-
# import selenium
import os
from datetime import datetime, timedelta
import time
import sys
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from collections import Counter
from konlpy.tag import Twitter
from pytz import timezone
import telegram



class start_blog:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver', chrome_options=options)
        self.driver.implicitly_wait(3)
        # self.start()
        self.bs4()



    def start(self):
        print("start")
        self.driver.get('http://finance.naver.com/sise/sise_low_up.nhn')
        self.driver.find_element_by_xpath('//*[@id="contentarea"]/div[3]/table/tbody')
        tr_list = self.driver.find_elements_by_css_selector('tr')
        for tr in tr_list:
            if not tr.text == "":
                print(tr.text)

    def bs4(self):
        bot = telegram.Bot(token='485029394:AAEMIt1L0HkolhN-wpQ8aWLJh3J7zT-sNFk')
        chat_id = bot.getUpdates()[-1].message.chat.id
        html = requests.get('http://finance.naver.com/sise/sise_low_up.nhn').text
        soup = bs(html, 'html.parser')
        table = soup.find("table", {"class": "type_2"})
        aa = table.find_all("tr")
        list = []
        for count in range(0,len(aa)):
            # print(name.text)
            if not aa[count].text == "":
                if not count == 0:
                    # list.append(aa[count].text)
                    # print(' '.join(aa[count].text.split('\n')).replace("\t",""))
                    # print(aa[count].text.split('\n')[1:5])
                    # print(aa[count].text.split('\n')[7].replace("\t",""))
                    if count <18:
                        try:
                            # print(aa[count].text.split('\n')[1:5])
                            print(aa[count].text.split('\n')[1]+"위")
                            print("변동률 : "+aa[count].text.split('\n')[2])
                            print("종목이름 : "+ aa[count].text.split('\n')[3])
                            print("현재가격 : " + aa[count].text.split('\n')[4])
                            print(aa[count].find("img").get('alt', ''))
                            print("-------------------------------")
                            list.append(aa[count].text.split('\n')[1]+"위\n"+"변동률 : "+aa[count].text.split('\n')[2]+'\n'+"종목이름 : "+ aa[count].text.split('\n')[3]+'\n'+"현재가격 : " + aa[count].text.split('\n')[4]+'\n'+aa[count].find("img").get('alt', '')+"-------------------------------"+'\n')
                            # print(aa[count].find("img").get('alt',''))
                        except Exception as e:
                            print(str(e))
                        bot.sendMessage(chat_id=chat_id, text=list)


start_blog()