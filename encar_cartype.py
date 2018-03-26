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
        self.driver.get(
            "https://m.encar.com/index.do?firstFg=Y&WT.hit=index_mobile_1st#/optManufact?intent=%7B%22type%22%3A%22car%22%2C%22action%22%3A%22(And.Hidden.N._.(Or.CarType.Y._.CarType.N.))%22%2C%22toggle%22%3A%7B%22modelGroup%22%3A1%7D%2C%22layer%22%3A%22optManufact%22%7D")
        # self.foreign_car()
        self.domestic_car()
        # self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))



    def domestic_car(self):
        # print(self.BASE_DIR)
        self.driver.get(
            "https://m.encar.com/index.do?firstFg=Y&WT.hit=index_mobile_1st#/optManufact?intent=%7B%22type%22%3A%22car%22%2C%22action%22%3A%22(And.Hidden.N._.(Or.CarType.Y._.CarType.N.))%22%2C%22toggle%22%3A%7B%22modelGroup%22%3A1%7D%2C%22layer%22%3A%22optManufact%22%7D")

        print("국산차")
        domestic_car = self.driver.find_element_by_xpath('//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[1]')
        self.car_brand_list = domestic_car.find_elements_by_css_selector('dd.item')
        self.car_search()
        # for count in range(1, len(car_brand_list)):
        #         # self.driver.find_element_by_xpath('# // *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[1] / dd['+str(count)+'] / button').click()
        #     self.driver.find_element_by_xpath('//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[1]/dd['+str(count)+']/button').click() # 국산용
        #     time.sleep(3)
        #
        #     try:
        #         car_list = self.driver.find_element_by_xpath('//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]')
        #         # car_list_name = car_list.find_element_by_css_selector('dd.item')
        #         car_list_name = car_list.find_elements_by_class_name('item')
        #         print(len(car_list_name))
        #         for i in range(1, len(car_list_name)):
        #             car_name = self.driver.find_element_by_xpath('// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl[2] / dd['+str(i)+']').text
        #             car_name_number = car_name.split('\n')[1]
        #             car_name = car_name.split('\n')[0]
        #             if car_name_number != "0":
        #                 print("car_name:" + car_name)
        #                 f = open('./car_name_list.txt', 'a')
        #                 f.write(car_name + "\n")
        #                 f.close()
        #             # f = open('./car_name_list.txt', 'a')
        #             # f.write(car_name+"\n")
        #             # f.close()
        #     except Exception as e:
        #         print(str(e))
        #         car_list = self.driver.find_element_by_xpath(
        #             '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl')
        #         car_list_name = car_list.find_elements_by_class_name('item')
        #         for i in range(1, len(car_list_name)):
        #             car_name = self.driver.find_element_by_xpath(
        #                 '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[' + str(i) + ']').text
        #             car_name_number = car_name.split('\n')[1]
        #             car_name = car_name.split('\n')[0]
        #             if car_name_number != "0":
        #                 print("car_name:" + car_name)
        #                 f = open('./car_name_list.txt', 'a')
        #                 f.write(car_name + "\n")
        #                 f.close()
        #
        #     self.driver.back()
        #     time.sleep(2)

    def foreign_car(self):
        print("수입차")
        foreign_car = self.driver.find_element_by_xpath('//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[3]')
        self.car_brand_list = foreign_car.find_elements_by_css_selector('dd.item')
        self.car_search()


    def car_search(self):

        for count in range(1, len(self.car_brand_list)+1):
            print("count:"+str(count))
                # self.driver.find_element_by_xpath('# // *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[1] / dd['+str(count)+'] / button').click()
            # self.driver.find_element_by_xpath('//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[1]/dd['+str(count)+']/button').click() # 국산용
            # car_brand_name = self.driver.find_element_by_xpath(
            #     '//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[3]/dd[' + str(count) + ']/button').text # 수입용
            car_brand_name = self.driver.find_element_by_xpath(
                '//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[1]/dd[' + str(count) + ']/button').text # 국산용
            car_brand_name = car_brand_name.split('\n')[0]
            print(car_brand_name)

            # self.driver.find_element_by_xpath('//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[3]/dd['+str(count)+']/button').click()  # 수입용
            self.driver.find_element_by_xpath(
                '//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[1]/dd[' + str(count) + ']/button').click()  # 국산용
            time.sleep(3)

            try:
                car_list = self.driver.find_element_by_xpath('//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]')
                # car_list_name = car_list.find_element_by_css_selector('dd.item')
                car_list_name = car_list.find_elements_by_class_name('item')
                print(len(car_list_name))
                for i in range(1, len(car_list_name)+1):
                    car_name = self.driver.find_element_by_xpath('// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl[2] / dd['+str(i)+']').text
                    car_name_number = car_name.split('\n')[1]
                    car_name = car_name.split('\n')[0]
                    if car_name_number != "0":
                        print("car_name:" + car_name)
                        f = open('./car_name_list_2.txt', 'a')
                        f.write(car_brand_name + " " + car_name + "\n")
                        f.close()
                    # f = open('./car_name_list.txt', 'a')
                    # f.write(car_name+"\n")
                    # f.close()
            except Exception as e:
                print(str(e))
                car_list = self.driver.find_element_by_xpath(
                    '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl')
                car_list_name = car_list.find_elements_by_class_name('item')
                for i in range(1, len(car_list_name)+1):
                    car_name = self.driver.find_element_by_xpath(
                        '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[' + str(i) + ']').text
                    car_name_number = car_name.split('\n')[1]
                    car_name = car_name.split('\n')[0]
                    if car_name_number != "0":
                        print("car_name:" + car_name)
                        f = open('./car_name_list_2.txt', 'a')
                        f.write(car_brand_name+" "+car_name + "\n")
                        f.close()

            self.driver.back()
            time.sleep(2)

start_class(interval=60)