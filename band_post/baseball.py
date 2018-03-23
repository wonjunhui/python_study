# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
import requests
from datetime import datetime



class Encar_class:
    def __init__(self, interval=60):
        self.car_name = ""
        self.brand_name = ""
        self.i = ""
        self.list_out = []
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        # self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver', chrome_options=options)
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
        self.driver.implicitly_wait(3)
        self.login()
        # self.start()
        # self.car_type()
        # self.Lotte_Data()
        # self.Most_view()
        # self.Foreign_Most_view()

        # while True:
        #
        #     now = datetime.now().strftime("%H:%M:%S")
        #     if now == "12:08:00":
        #         print("현재시간 : "+now)
        #         options = webdriver.ChromeOptions()
        #         options.add_argument('headless')
        #         options.add_argument('window-size=1920x1080')
        #         options.add_argument("disable-gpu")
        #
        #         self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver', chrome_options=options)
        #         self.driver.implicitly_wait(3)
        #         time.sleep(60)

    def Lotte_Data(self):
        print("----------롯데 데이터----------")
        self.driver.get('http://sports.news.naver.com/kbaseball/news/index.nhn?type=team&team=LT')
        news_list = self.driver.find_element_by_xpath('//*[@id="_newsList"]/ul')
        news_list_div = news_list.find_elements_by_css_selector('li')
        news_list_a = news_list.find_elements_by_css_selector('a')
        # print(news_list_div)

        for news in news_list_div:
            news_a = news.find_element_by_css_selector('a')
            print(news.text)
            print("URL: "+news_a.get_attribute("href")+'\n')

        # for link in news_list_a:
        #     print("URL: "+link.get_attribute("href"))

        # req = requests.get('http://sports.news.naver.com/kbaseball/news/index.nhn?type=team&team=LT')
        # # HTML 소스 가져오기
        # html = req.text
        # # BeautifulSoup으로 html소스를 python객체로 변환하기
        # # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
        # # 이 글에서는 Python 내장 html.parser를 이용했다.
        # soup = BeautifulSoup(html, 'html.parser')
        # table = soup.find(id="_newsList")
        # ul = table.find("ul")
        # print(soup)
        # news_1 = ul.find_all("li")
        # for news in news_1:
        #     print(news.get_text())

    def Most_view(self):
        print("----------국내 많이 본 뉴스----------")
        rank_news = self.driver.find_element_by_xpath('//*[@id="rankingNewsList_0"]')
        rank_news_li = rank_news.find_elements_by_css_selector('li')
        # rank_news_a = rank_news.find_elements_by_css_selector('a')

        for news in rank_news_li:
            news_a = news.find_element_by_css_selector('a')
            print(news.text)
            print("URL: "+news_a.get_attribute("href")+'\n')


    def Foreign_Most_view(self):
        print("----------해외 많이 본 뉴스----------")
        self.driver.get('http://sports.news.naver.com/wbaseball/news/index.nhn?type=popular')
        rank_news = self.driver.find_element_by_xpath('//*[@id="rankingNewsList_0"]')
        rank_news_li = rank_news.find_elements_by_css_selector('li')
        # rank_news_a = rank_news.find_elements_by_css_selector('a')

        for news in rank_news_li:
            news_a = news.find_element_by_css_selector('a')
            print(news.text)
            print("URL: "+news_a.get_attribute("href")+'\n')

    def login(self):
        self.account = dict()
        with open("./bandaccount.txt", 'rt') as fp:
            data = fp.readlines()
            for d in data:
                d = d.split(" ")
                self.account[d[0]] = d[1]
            fp.close()

        self.driver.get('https://band.us/band/51905190')
        self.driver.find_element_by_xpath('//*[@id="login_list"]/li[1]/a').click()
        self.driver.find_element_by_id("input_local_phone_number").send_keys(self.account["phone"])
        time.sleep(2)
        self.driver.find_element_by_id("input_password").send_keys(self.account["pwd"])
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="phone_login_form"]/button').click()
        # time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/section/div[2]/div/button').click()
        # self.driver.find_element_by_class_name('contentEditor._richEditor.skin10.cke_editable.cke_editable_inline.cke_contents_ltr').send_keys("하이하이하이하이")
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]').click()
        # self.driver.find_element_by_class_name('gSrOnly').send_keys("하이")
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div').send_keys("하이")
        time.sleep(10)

Encar_class(interval=60)