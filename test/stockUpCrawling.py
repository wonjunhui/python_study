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
# import telegram



class start_blog:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver',chrome_options=options)
        self.driver.implicitly_wait(3)
        self.start()
        # self.bs4()



    def start(self):
        print("start")
        self.driver.get('https://page.kakao.com/main?categoryUid=10&subCategoryUid=1000&navi=1&inkatalk=0&inChannel=0')
        self.driver.find_element_by_xpath('//*[@id="root"]/div[3]/div[3]/div[3]/ul/li[2]/a/div[2]/span[1]/p').click()
        time.sleep(5)

        print(self.driver.page_source)
        f = open('kakao_source.txt', 'a')
        f.write(self.driver.page_source)
        f.close()
        # self.driver.get('http://finance.naver.com/sise/sise_low_up.nhn')
        # self.driver.find_element_by_xpath('//*[@id="contentarea"]/div[3]/table/tbody')
        # tr_list = self.driver.find_elements_by_css_selector('tr')
        # for tr in tr_list:
        #     if not tr.text == "":
        #         print(tr.text)




start_blog()