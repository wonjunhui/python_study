# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException


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

        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver', chrome_options=options)
        self.driver.implicitly_wait(3)
        # self.start()
        self.car_type()


    def car_type(self):
        self.driver.get(
            "https://m.encar.com/index.do?firstFg=Y&WT.hit=index_mobile_1st#/optManufact?intent=%7B%22type%22%3A%22car%22%2C%22action%22%3A%22(And.Hidden.N._.(Or.CarType.Y._.CarType.N.))%22%2C%22toggle%22%3A%7B%22modelGroup%22%3A1%7D%2C%22layer%22%3A%22optManufact%22%7D")
        # car_brand_list = self.driver.find_element_by_xpath('//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[1]')
        # car_brand_list_dl = car_brand_list.find_elements_by_css_selector('dd.item')

        # for item in car_brand_list_dl:
        #     print(item.text)

        car_brand_list = self.driver.find_element_by_xpath('// *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[3]') # 수입차용
        # car_brand_list = self.driver.find_element_by_xpath(
        #     '// *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[1]')  # 국산용
        car_brand_list_dl = car_brand_list.find_elements_by_css_selector('dd.item')

        # // *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[3] / dd[11] / button
        print("car_brand_list:"+str(len(car_brand_list_dl)))
        try:
            for count in range(56,len(car_brand_list_dl)+1):
                # brand_name = car_brand_list_dl[count].text
                self.list_out = []
                # print(brand_name)
                # print(car_brand_list_dl[2].text)
                count = str(count)
                # self.brand_name = self.driver.find_element_by_xpath('// *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[1] / dd['+count+'] / button').text # 국산용
                self.brand_name = self.driver.find_element_by_xpath('// *[ @ id = "optManufact"] / div[2] / div / div / div[2] / dl[3] / dd['+count+'] / button').text # 수입차용
                self.brand_name = self.brand_name.split('\n')[0]
                print(self.brand_name)
                # self.driver.find_element_by_xpath('//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[1]/dd['+count+']/button').click() # 국산용
                self.driver.find_element_by_xpath('//*[@id="optManufact"]/div[2]/div/div/div[2]/dl[3]/dd['+count+']/button').click() # 수입차용
                time.sleep(2)
                self.start()
                self.driver.back()
        except Exception as e:
            print("car_type:"+str(e))

    def start(self):
        # self.driver.get(
        #     "https://m.encar.com/index.do?firstFg=Y&WT.hit=index_mobile_1st#/optModel?intent=%7B%22type%22%3A%22car%22%2C%22action%22%3A%22(And.Hidden.N._.(C.CarType.Y._.Manufacturer.%ED%98%84%EB%8C%80.))%22%2C%22toggle%22%3A%7B%22modelGroup%22%3A1%7D%2C%22layer%22%3A%22optModel%22%7D")
        search_url = "https://m.encar.com/ca/search.do"
        html = self.driver.page_source  # 페이지의 elements모두 가져오기
        soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup사용하기
        try:
            car_name_list = self.driver.find_element_by_xpath(
                '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl[2]')
               # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl[2]
            # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl
        except Exception as e:
            print("onlyNameList"+str(e))
            car_name_list = self.driver.find_element_by_xpath('//*[@id="optModel"]/div[2]/div[2]/div/div/dl')
            # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl
                # '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl')
        # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[2] / button

        car_name_list_dl = car_name_list.find_elements_by_css_selector('dd.item')
        # print(len(car_name_list_dl))
        # print(car_name_list)
        # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[1] / button
        print("total_car_name_list:"+str(len(car_name_list_dl)))
        try:
            for i in range(1, len(car_name_list_dl)+1):
                i = str(i)
                # i="28"
                self.i = i
                print("i=" + i)

                try:
                    print("선택 완료")
                    self.driver.find_element_by_xpath(
                        '//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]/dd[' + i + ']/button').click()  # 첫페이지 차종 클릭
                    # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl[2] / dd[1] / button
                    # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl[2] / dd[3] / button
                    self.car_detail()
                    self.driver.back()
                except Exception as e:
                    print("click_2:"+str(e))
                    try:
                        # self.car_name = self.driver.find_element_by_xpath('//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd['+self.i+']/button').text #추천차량 없을때
                        self.car_name = self.driver.find_element_by_xpath(
                            '//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]/dd[' + self.i + ']/button').text #추천차량 있을때

                        self.driver.find_element_by_xpath(
                            '//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]/dd[' + self.i + ']/button').click()
                        self.car_detail()
                        self.driver.back()

                        self.car_name = self.car_name.split('\n')[0]
                        # self.car_name = self.car_name.replace("삭제", "")
                        print("첫페이지 차종 없을시_1:"+self.car_name)
                    except Exception as e:
                        try:
                            print("제발 :"+str(e))
                            self.car_name = self.driver.find_element_by_xpath(
                                '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + self.i + ']/button').text
                            self.driver.find_element_by_xpath('//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + self.i + ']/button').click()

                            self.car_detail()
                            self.driver.back()

                            # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[4] / button

                            self.car_name = self.car_name.split('\n')[0]
                            # self.car_name = self.car_name.replace("삭제", "")
                            print("첫페이지 차종 없을시_2:" + self.car_name)
                        except Exception as e:
                            print("제발2"+str(e))
                            try:
                                print(self.driver.find_element_by_xpath(
                                    '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + self.i + ']/ul'))
                                self.fuel_catch()
                                self.driver.back()
                                time.sleep(1)
                                self.driver.back()
                                time.sleep(1)
                                print("123123: " + str(e))

                            except Exception as e:
                                print("text:" + str(e))
                                self.driver.find_element_by_xpath(
                                    '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + i + ']/button').click()  # 첫페이지 차종 클릭
                                self.car_detail()
                                self.driver.back()

        except Exception as e:
            print("start Exception :"+str(e))


    def car_detail(self):

        car_list = ""
        car = ""
        j_2=1

        try:
            car_list = self.driver.find_element_by_xpath('// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl[2] / dd['+self.i+'] / ul')
            car = car_list.find_elements_by_css_selector("li.item")
            self.car_name = self.driver.find_element_by_xpath(
                '// *[ @ id = "searchCondition1"] / div[1] / ul / li[2] / button / span[1] / var').text
            self.fuel_catch()
            self.driver.back()
            time.sleep(1)
            self.driver.back()
            time.sleep(1)

            print("car=" + str(len(car)))
            for j in range(1, len(car) + 1):
                j = str(j)
                j_2 = j
                print("j_1=" + j)
                try:
                    self.car_name = self.driver.find_element_by_xpath(
                        '//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]/dd[' + self.i + ']/ul/li[' + j + ']/button').text
                    # self.car_name = self.car_name.split('\n')[0]
                    print("car_name:" + self.car_name)
                    self.driver.find_element_by_xpath(
                        '//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]/dd[' + self.i + ']/ul/li[' + j + ']/button').click()
                except Exception as e:
                    print("NOCARNAME_1:"+str(e))
                    # self.car_name = self.driver.find_element_by_xpath(
                    #     '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + j + ']/button').text
                    self.driver.find_element_by_xpath(
                        '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + self.i + ']/ul/li['+j+']/button').click()
                    # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[2] / ul / li[1] / button
                    # // *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[4] / button
                self.car_name = self.car_name.split('\n')[0]

                time.sleep(1)
                # self.car_name = self.driver.find_element_by_css_selector('li.cond_model')
                # self.car_name.text.replace(" ","")
                # print("fhfh:" + self.car_name)
                time.sleep(1)
                self.fuel_catch()
                self.driver.back()
                time.sleep(1)
                self.driver.back()
                time.sleep(1)

        except Exception as e:
            print("CarDetailException:"+str(e))

            try:
                car_list = self.driver.find_element_by_xpath('// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd['+self.i+'] / ul')

                car = car_list.find_elements_by_css_selector("li.item")
                print("len(car):"+str(len(car)))
                for j in range(1, len(car) + 1):
                    j = str(j)
                    j_2 = j
                    print("j_2=" + j)
                    try:
                        self.car_name = self.driver.find_element_by_xpath(
                            '//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]/dd[' + self.i + ']/ul/li[' + j + ']/button').text
                        # self.car_name = self.car_name.split('\n')[0]
                        print("car_name:" + self.car_name)
                        self.driver.find_element_by_xpath(
                            '//*[@id="optModel"]/div[2]/div[2]/div/div/dl[2]/dd[' + self.i + ']/ul/li[' + j + ']/button').click()
                        self.car_name = self.car_name.split('\n')[0]

                        time.sleep(1)
                        # self.car_name = self.driver.find_element_by_css_selector('li.cond_model')
                        # self.car_name.text.replace(" ","")
                        # print("fhfh:" + self.car_name)
                        # time.sleep(1)
                        self.fuel_catch()
                        self.driver.back()
                        time.sleep(1)
                        self.driver.back()
                        time.sleep(1)
                    except Exception as e:
                        print("NOCARNAME:" + str(e))
                        try:
                            self.driver.find_element_by_xpath(
                                '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + self.i + ']/ul/li[' + j + ']/button').click()
                            self.car_name = self.driver.find_element_by_xpath(
                                '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[' + self.i + '] / ul / li[' + str(
                                    j) + '] / button').text
                            print("car_name_detail:" + self.car_name)
                            print("jj= " + str(j))
                            self.car_name = self.car_name.split('\n')[0]
                            self.car_name = self.car_name.replace("삭제", "")
                            self.fuel_catch()
                            self.driver.back()
                            time.sleep(1)
                            self.driver.back()
                            time.sleep(1)
                            print("상세진입")
                        except Exception as e:
                            print("NOCARNAME_3:"+str(e))
                            self.car_name = self.driver.find_element_by_xpath(
                                '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[' + self.i + '] / ul / li[' + str(
                                    j) + '] / button').text
                            print("car_name_detail:" + self.car_name)
                            print("jj= " + str(j))
                            self.car_name = self.car_name.split('\n')[0]
                            self.car_name = self.car_name.replace("삭제", "")
                            self.fuel_catch()
                            self.driver.back()
                            time.sleep(1)
                            self.driver.back()
                            time.sleep(1)


                print("tete")
            except Exception as e:
                try:
                    print("CarDetailException_2:"+str(e))
                    print(self.car_name)
                    total_car = self.driver.find_element_by_xpath('// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl')
                    car_list = self.driver.find_element_by_xpath(
                        '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd['+self.i+']/ul')
                    car = car_list.find_element_by_css_selector('li.item').text

                    print("car2=" + str(len(car)))
                    for count in range(1, len(car)+1):
                        self.car_name = self.driver.find_element_by_xpath(
                            '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd['+self.i+'] / ul / li['+str(count)+'] / button').text
                        print("exception:" + self.car_name)
                        print("count= "+str(count))
                        self.car_name = self.car_name.split('\n')[0]
                        self.car_name = self.car_name.replace("삭제", "")
                        self.driver.find_element_by_xpath('//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd['+self.i+']/ul/li['+str(count)+']/button').click()
                        self.fuel_catch()
                        self.driver.back()
                        time.sleep(1)
                        self.driver.back()
                        time.sleep(2)
                except Exception as e:
                    print("CarDetailException_3"+str(e))
                    try:
                        self.driver.find_element_by_xpath('// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[2] / button').click()
                        car_list = self.driver.find_element_by_xpath(
                            '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + self.i + ']/ul')
                        car = car_list.find_element_by_css_selector('li.item').text

                        print("car2=" + str(len(car)))
                        for count in range(1, len(car) + 1):
                            self.car_name = self.driver.find_element_by_xpath(
                                '// *[ @ id = "optModel"] / div[2] / div[2] / div / div / dl / dd[' + self.i + '] / ul / li[' + str(
                                    count) + '] / button').text
                            print("exception:" + self.car_name)
                            print("count= " + str(count))
                            self.car_name = self.car_name.split('\n')[0]
                            self.car_name = self.car_name.replace("삭제", "")
                            self.driver.find_element_by_xpath(
                                '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + self.i + ']/ul/li[' + str(
                                    count) + ']/button').click()
                            self.fuel_catch()
                            self.driver.back()
                            time.sleep(1)
                            self.driver.back()
                            time.sleep(1)
                    except Exception as e:
                        print("CarDetailException_4: "+str(e))
                        self.car_name = self.driver.find_element_by_xpath('// *[ @ id = "searchCondition1"] / div[1] / ul / li[2] / button / span[1] / var').text
                        self.car_name = self.car_name.split('\n')[0]
                        self.car_name = self.car_name.replace("삭제", "")
                        # self.driver.get('https://m.encar.com/ca/search.do?WT.hit=mWeb_SideMenu_CarSearch#!%7B%22type%22%3A%22car%22%2C%22action%22%3A%22(And.Hidden.N._.(C.CarType.Y._.Manufacturer.%EC%8C%8D%EC%9A%A9.))%22%2C%22toggle%22%3A%7B%22modelGroup%22%3A1%7D%2C%22layer%22%3A%22optModel%22%7D')
                        # time.sleep(2)
                        # self.driver.find_element_by_xpath(
                        #     '//*[@id="optModel"]/div[2]/div[2]/div/div/dl/dd[' + self.i + ']/button').click()  # 첫페이지 차종 클릭
                        print("성공")
                        self.fuel_catch()
                        self.driver.back()
                        time.sleep(1)
                        # self.driver.back()
                        time.sleep(1)



    def fuel_catch(self):

        print("fuel_catch")
        self.driver.find_element_by_xpath('// *[ @ id = "searchCondition1"] / div[3] / ul / li[1] / button').click()

        list = self.driver.find_elements_by_class_name("item")
        print("fdf:" + self.car_name)

        for item in list:

            stripText = item.text
            # item.text.replace(" ", "")
            # stripText = stripText.split('\n')
            # print("stripText1:" + stripText)
            if stripText != "" and stripText.split('\n')[1] != "0":
                print(stripText.split('\n')[1])
                self.list_out.append({'name': self.car_name, '연료': stripText.split('\n')[0], 'car_brand_name': self.brand_name, 'car_type':""})
                f = open('total_car_list.txt', 'a')
                f.write(self.car_name + "|" + stripText.split('\n')[0] + "|" + self.brand_name + "|" + " " + "|" + '\n')
                f.close()

                # if span.find_all("class:count") != "0":
                # print("stripText:"+stripText)

        # time.sleep(1)
        # pandasFrame = pd.DataFrame(self.list_out)
        # pandasFrame.to_csv('total_1.csv')

        # f = open('test_1.csv', 'w', encoding='utf-8', newline='')
        # wr = csv.writer(f)
        # print(self.list_out)
        # wr.writerows(self.list_out)
        # f.close()
        print("저장")


Encar_class(interval=60)
