# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException

class Navercar_class:
    def __init__(self, interval=60):
        self.car_name = ""
        self.brand_name = ""
        self.i = ""
        self.list_out = []
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver', chrome_options=options)
        self.driver.implicitly_wait(3)
        # self.start()
        self.search()


    def search(self):

        f = open('car_name_list_2.txt','r')
        data = f.readlines()
        for keyword in data:
            # print(keyword)
            kw = keyword.split()
            # query = keyword[0]+"+"+keyword[1]
            print(kw)
            self.driver.get('https://auto.naver.com/search/baseSearch.nhn?query=' + str(kw[0]) + '+' + str(kw[1]))
            try:
                info = self.driver.find_element_by_css_selector('li.info').text
                info = info.split()
                info = info[1]
                print(info)
                success = open('success_cartype.text','a')
                success.write(kw[0] +" "+ kw[1] + info +'\n')
                success.close()
                # self.driver.find_element_by_name('query').send_keys(keyword)
                # self.driver.find_element_by_xpath('//*[@id="baseSearchForm"]/fieldset/div/button[1]').click()
                time.sleep(1)
                # ul = self.driver.find_element_by_class_name('model_list result')
                URL = "https://auto.naver.com/search/baseSearch.nhn?query='+str(kw[0])+'+'+str(kw[1])"
                req = requests.get(URL)
                # HTML 소스 가져오기
                html = req.text

                soup = BeautifulSoup(html, 'html.parser')
            except Exception as e:
                print("하이"+str(e))
                failure = open('failure_cartype.txt','a')
                failure.write(kw[0] +" "+ kw[1] +'\n')
                failure.close()
            # div = soup.find('div',{'id':'content_wrap'})
            # ul = div.find('ul',{'class':'model_lst'})
            #
            # print(ul)
            self.driver.back()
# //*[@id="carSearchListArea"]/ul/li[2]/div/ul/li[4]/a/span
Navercar_class(interval=60)
