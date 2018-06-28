# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
from urllib.request import urlopen

class start:
    def __init__(self, interval=60):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver',chrome_options=options)
        self.driver.implicitly_wait(3)
        # self.car_people()
        # self.csv_modify()
        self.car_image_scrap()


    def car_people(self):
        f = open('car_name_list.txt', 'r')
        data = f.readlines()
        for keyword in data:
            # print(keyword)
            kw = keyword.split()
            # query = keyword[0]+"+"+keyword[1]
            print(kw)
            self.driver.get('https://auto.naver.com/search/baseSearch.nhn?query=' + str(kw[0]) + '+' + str(kw[1]))
            try:
                self.driver.find_element_by_xpath('//*[@id="carSearchListArea"]/ul/li[1]/div/div/span/a').click()
                self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[2]/a').click()

                car_list = self.driver.find_elements_by_css_selector('div.btm_col.main_info')
                print(str(len(car_list)))
                info = self.driver.find_elements_by_css_selector('li._line_5')
                for people in info:
                    if not people.text == "승차인원" or people.text == " " or people.text == "\n" or people.text == "정보없음":

                # info = info.split()
                # info = info[1]
                        print(people.text)
                        success = open('success_carpeople.text', 'a')
                        success.write(kw[0] + " " + kw[1] + " " + people.text + '\n')
                        success.close()
                # self.driver.find_element_by_name('query').send_keys(keyword)
                # self.driver.find_element_by_xpath('//*[@id="baseSearchForm"]/fieldset/div/button[1]').click()
                #     time.sleep(1)
                # ul = self.driver.find_element_by_class_name('model_list result')
                # URL = "https://auto.naver.com/search/baseSearch.nhn?query='+str(kw[0])+'+'+str(kw[1])"

                # req = requests.get(URL)
                # # HTML 소스 가져오기
                # html = req.text
                #
                # soup = BeautifulSoup(html, 'html.parser')
            except Exception as e:
                print("하이" + str(e))
                failure = open('failure_carpeople.txt', 'a')
                failure.write(kw[0] + " " + kw[1] + '\n')
                failure.close()
            # div = soup.find('div',{'id':'content_wrap'})
            # ul = div.find('ul',{'class':'model_lst'})
            #
            # print(ul)
            self.driver.back()






    def suv_car(self):

        url = 'https://auto.naver.com/car/carKindType.nhn?carKndCd=5&carKndTpCatCd=OWD&importYn=Y'
        html = urlopen(url)
        source = BeautifulSoup(html.read(), "html.parser")
        ul = source.find("ul",class_="model_lst")
        name = ul.findAll("span",class_="box")

        for i in range(2,21):
            url = 'https://auto.naver.com/car/carKindType.nhn?carKndCd=5&carKndTpCatCd=OWD&importYn=Y&page='+str(i)
            html = urlopen(url)
            source = BeautifulSoup(html.read(), "html.parser")
            ul = source.find("ul", class_="model_lst")
            name = ul.findAll("span", class_="box")

            for name_detail in name:
                print(name_detail.text.split(' ')[1:])
                wordlist = name_detail.text.split(' ')[1:]
                word = ''.join(map(str,wordlist))
                print(word)
                f = open('sub_rv.txt', 'a')
                # f.write(name_detail.text.split(' ')[1:].join + '\n')
                f.write(word+'\n')
                f.close()

    def csv_modify(self):
        df = pd.read_csv('./total_1_1.csv',index_col=0)
        for count in range(0,len(df)):
            df["car_name_detail"][count] = df["car_name_detail"][count][0:-8]
            # print(df.index[1])
            # print(len(df["car_name_detail"][count]))

        # print(df)
        # df.to_csv('./total_1_2.csv')

    def car_image_scrap(self):
        self.driver.get('https://auto.naver.com/car/mainList.nhn?isMnfcoAll=Y')
        ul = self.driver.find_element_by_xpath('//*[@id="_vendor_select_layer"]/div/div[1]/div[2]/ul')
        lists = ul.find_elements_by_css_selector('li')
        print(str(len(lists))+"개")
        # self.driver.find_element_by_xpath('//*[@id="_vendor_select_layer"]/div/div[1]/div[2]/ul/li[1]')

        # print(str(len(df)))
start(interval=10)
# div = source.find("div",class_="paginate2")
# print(str(len(div)))
# print(name[0].text)

# https://auto.naver.com/company/main.nhn?mnfcoNo=16&modelType=OS&&order=0&importYn=N
# https://auto.naver.com/company/main.nhn?mnfcoNo=16&modelType=DC&order=0&importYn=N

# https://auto.naver.com/company/main.nhn?mnfcoNo=16&importYn=N
# https://auto.naver.com/company/main.nhn?mnfcoNo=12&importYn=N
110
# 84+26