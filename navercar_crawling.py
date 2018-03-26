# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
import os

class start_class:
    def __init__(self, interval=60):
        self.brand_list = []
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
        self.driver.implicitly_wait(3)
        # self.load_brand_name()
        # self.add_brand_name()
        self.car_brand_list = []
        self.car_type_crawling()
        # self.domestic_car()
        # self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def car_type_crawling(self):
        self.driver.get(
            "https://auto.naver.com/car/mainList.nhn")
        self.driver.find_element_by_name('query').send_keys('아반떼')
        self.driver.find_element_by_xpath('//*[@id="baseSearchForm"]/fieldset/div/button[1]').click()
        list_1 = self.driver.find_element_by_xpath('// *[ @ id = "carSearchListArea"] / ul / li[1]')
        span = self.driver.find_element_by_xpath('//*[@id="carSearchListArea"]/ul/li[1]/div/ul/li[4]/a/span').text
        print(span)
        time.sleep(10)


start_class(interval=60)