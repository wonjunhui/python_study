# -*- coding: utf-8 -*-
import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
import codecs

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
import os
# import sys


# df = pd.read_csv('./testdaedong.csv')
# df.to_csv('./testdaedong.csv', index = False, header = False)

class start_class:
    def __init__(self, interval=60):
        self.brand_list = []
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
        self.driver.implicitly_wait(3)
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # self.load_brand_name()
        self.add_brand_name_2()

    def load_brand_name(self):
        self.driver.get(
            "https://m.encar.com/index.do?firstFg=Y&WT.hit=index_mobile_1st#/optManufact?intent=%7B%22type%22%3A%22car%22%2C%22action%22%3A%22(And.Hidden.N._.(Or.CarType.Y._.CarType.N.))%22%2C%22toggle%22%3A%7B%22modelGroup%22%3A1%7D%2C%22layer%22%3A%22optManufact%22%7D")
        car_brand_list_1 = self.driver.find_element_by_xpath('// *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[3]') # 수입차용
        car_brand_list_2 = self.driver.find_element_by_xpath(
            '// *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[1]')  # 국산용
        car_brand_list_dl_1 = car_brand_list_2.find_elements_by_css_selector('dd.item')
        car_brand_list_dl_2 = car_brand_list_1.find_elements_by_css_selector('dd.item')

        car_list = []

        f = open(os.path.join(self.BASE_DIR, 'foreign_car.txt'), 'a')
        try:

            for count in range(1, len(car_brand_list_dl_2)+1):
                count = str(count)
                domestic_car = self.driver.find_element_by_xpath('// *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[3] / dd['+count+'] / button').text
                domestic_car = domestic_car.split('\n')[0]
                car_list.append(domestic_car)
                print(domestic_car)
                # lines = f.readline()

                f.write(domestic_car + '\n')
            # lines = f.readlines()
            # for line in lines:
            #     print(line)
            f.close()


        except Exception as e:
            print(str(e))




    def add_brand_name(self):
        # self.driver.close()
        print(self.BASE_DIR)
        f = open(os.path.join(self.BASE_DIR, 'foreign_car.txt').encode('euc-kr'),'rb')
        lines = f.readlines()
        print(lines)
        for line in lines:
            # line = line.split('\n')[0]
            # line = line.decode('utf8', 'ignore')
            # line = line.decode('euc-kr')
            # line = line.decode('utf-8')

            try:
                line = line.split('\n')[0]
                print(line)
                # line= line.encode('utf-8').strip()
                df = pd.read_csv('/Users/wonjunhui/testtrade/car_brand_data/foreign_car/'+str(line)+'_1.csv', index_col=0,sep=None,error_bad_lines=False, delimiter=',',encoding='utf8', engine='python')
                # df["brand_name"] = line
                df["car_type"] = ""
                df.to_csv('/Users/wonjunhui/testtrade/car_brand_data/foreign_car/'+str(line)+'_1.csv')

                # dd = open('/Users/wonjunhui/testtrade/car_brand_data/domestic_car/'+str(line)+'_1.csv', 'r', encoding='utf-8')
                # dd_2 = csv.reader(dd)
                # for row in dd_2:
                #     print(row)
                # df.to_csv('./testdaedong.csv', index=False, header=False)
                print(df)
                time.sleep(1)

            except Exception as e:
                print(str(e))
                # df = pd.read_csv('/Users/wonjunhui/testtrade/car_brand_data/domestic_car/' + str(line) + '_1.csv',index_col=0, sep=',', engine='c')
                f = open(os.path.join(self.BASE_DIR, 'exception.txt'), 'a')
                f.write(line + '\n')
                f.close()


    def add_brand_name_2(self):
        matrix = []
        self.driver.close()
        line = "마세라티"
        # type(line)
        print(type(line))
        url = ''
        f = open('/Users/wonjunhui/testtrade/car_brand_data/domestic_car/기아_1 복사본.csv','r')
        reader = csv.reader(f)
        for row in reader:
            print(row)
        # with open('/Users/wonjunhui/testtrade/car_brand_data/foreign_car/' + str(line) + '_1.csv' , newline='', encoding='utf-8') as f:
        #     reader = csv.reader(f)
        #     for row in reader:
        #         print(row)

        # with open('/Users/wonjunhui/testtrade/car_brand_data/domestic_car/기아_1 복사본.csv', newline='') as csvfile:
        #     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #     for row in spamreader:
        #         print(', '.join(row))

        # infile = codecs.open('/Users/wonjunhui/testtrade/car_brand_data/domestic_car/제네시스_1.csv', 'r', encoding='euc-kr')
        # outfile = codecs.open('/Users/wonjunhui/testtrade/car_brand_data/domestic_car/제네시스_1.csv', 'w', encoding='utf-8')
        # for line in infile:
        #     line = line.replace(u'\xa0', ' ')  # 가끔 \xa0 문자열로 인해 오류가 발생하므로 변환
        #     print(line)
        #     outfile.write(line)
        #
        # infile.close()
        # outfile.close()


        # csvReader = csv.reader(f)
        #
        # for row in csvReader:
        #     matrix.append(row)
        #     print(row)

        # f.close()
        # line = line.decode('utf-8').strip()
        # line = line.decode('***').encode('utf-8')
        # line = str(line, 'utf-8')
        # line = line.decode('cp949')
        # line = line | iconv -f cp949 -t utf-8
        # df = pd.read_csv('/Users/wonjunhui/testtrade/car_brand_data/foreign_car/' + line + '_1.csv', index_col=0, sep=None, error_bad_lines=False, delimiter=',', encoding='utf8', engine='python')
        # df["brand_name"] = line
        # df["car_type"] = ""
        # df.to_csv('/Users/wonjunhui/testtrade/car_brand_data/foreign_car/' + line + '_1.csv')

start_class(interval=60)

