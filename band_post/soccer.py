# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
import requests
from datetime import datetime
from pytz import timezone
from PIL import Image
import os


class Encar_class:
    def __init__(self, interval=60):
        self.car_name = ""
        self.brand_name = ""
        self.i = ""
        self.list_out = []
        self.foreigntsr = ""
        self.lottestr = ""
        self.domesticstr = ""
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--disable-extensions')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
        # self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
        self.driver.implicitly_wait(3)
        # self.login()
        # self.start()
        # self.car_type()
        # self.Lotte_Data()
        self.Most_view()
        # self.Foreign_Most_view()
        # self.login()
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
        print("----------현재 인기 뉴스----------")
        self.driver.get('http://sports.news.naver.com/kbaseball/news/index.nhn?type=team&team=LT')
        news_list = self.driver.find_element_by_xpath('//*[@id="_newsList"]/ul')
        news_list_div = news_list.find_elements_by_css_selector('li')
        news_list_a = news_list.find_elements_by_css_selector('a')
        self.lottestr = "\n"
        # print(news_list_div)

        for news in news_list_div:
            news_a = news.find_element_by_css_selector('a')
            # self.lottestr= self.lottestr + '\n' + news.text + '\n' +news_a.get_attribute("href")
            self.lottestr = self.lottestr +'\n'+ news_a.get_attribute("href")

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
        print("----------현재 인기 뉴스----------")
        self.driver.get('http://sports.news.naver.com/wfootball/news/index.nhn')
        # width = self.driver.execute_script(
        #     "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);")
        # height = self.driver.execute_script(
        #     "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
        # self.driver.manage.window.resize_to(width + 100, height + 100)
        # time.sleep(2)
        # total_height = self.driver.execute_script("return document.body.parentNode.scrollHeight")
        # self.driver.set_window_size(default_width)
        #
        # img = self.driver.screenshot_as("/Users/wonjunhui/Desktop/sc.png")

        # self.driver.get('https://www.naver.com/')
        # fullpage_screenshot(self.driver,"screenshot.png")
        # self.driver.execute_script("window.scrollTo(0, 0);")
        # self.driver.maximize_window()
        # element = self.driver.find_element_by_tag_name('body')
        # element_png = element.screenshot_as_png
        # with open("test2.png", "wb") as file:
        #     file.write(element_png)
        # ("/Users/wonjunhui/Desktop/sc.png")
        # self.driver.get_screenshot_as_file("/Users/wonjunhui/Desktop/sc.png")
        rank_news = self.driver.find_element_by_xpath('//*[@id="rankingNewsList_0"]')
        rank_news_li = rank_news.find_elements_by_css_selector('li')
        # rank_news_a = rank_news.find_elements_by_css_selector('a')
        self.lottestr = "------현재 인기 뉴스------"
        for news in rank_news_li:
            news_a = news.find_element_by_css_selector('a')
            # self.domesticstr= self.domesticstr + '\n' + news.text + '\n' +news_a.get_attribute("href")
            self.lottestr = self.lottestr +'\n' + news_a.get_attribute("href")
            print(news.text)
            # print("URL: "+news_a.get_attribute("href")+'\n')



    def Foreign_Most_view(self):
        print("----------해외 많이 본 뉴스----------")
        self.foreigntsr = "------해외 많이 본 뉴스 10개 입니다------"


        self.driver.get('http://sports.news.naver.com/wbaseball/news/index.nhn?type=popular')
        rank_news = self.driver.find_element_by_xpath('//*[@id="rankingNewsList_0"]')
        rank_news_li = rank_news.find_elements_by_css_selector('li')
        # rank_news_a = rank_news.find_elements_by_css_selector('a')

        for news in rank_news_li:
            news_a = news.find_element_by_css_selector('a')
            # self.foreigntsr = self.foreigntsr + '\n' + news.text + '\n' +news_a.get_attribute("href")
            self.foreigntsr = self.foreigntsr +'\n'+ str(news_a.get_attribute("href"))
            print(news.text)
            print("링크: "+news_a.get_attribute("href")+'\n')
        # self.login()

    def login(self):
        self.account = dict()
        with open("./bandaccount.txt", 'rt') as fp:
            data = fp.readlines()
            for d in data:
                d = d.split(" ")
                self.account[d[0]] = d[1]
            fp.close()

        # self.driver.get('https://band.us/band/51905190') # 해적
        nowtime = datetime.now(timezone('Asia/Seoul')).strftime("%Y년 %m월 %d일")
        # self.driver.get('https://band.us/band/70593187') # 테스트
        self.driver.get('https://band.us/band/51380682') # 정상
        self.driver.find_element_by_xpath('//*[@id="login_list"]/li[1]/a').click()
        self.driver.find_element_by_id("input_local_phone_number").send_keys(self.account["phone"])
        time.sleep(2)
        self.driver.find_element_by_id("input_password").send_keys(self.account["pwd"])
        time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="phone_login_form"]/button').click()
        # time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/section/div[2]/div/button').click()
        time.sleep(2)
        # self.driver.find_element_by_class_name('contentEditor._richEditor.skin10.cke_editable.cke_editable_inline.cke_contents_ltr').send_keys("하이하이하이하이")
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]').click()
        # self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div/p').send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[4]/ul/li[1]/button').click()
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div').send_keys(nowtime+" 실시간 뉴스 입니다\n")
        # self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div').send_keys(self.foreigntsr)
        # self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div').send_keys('\n')
        # time.sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div').send_keys(self.domesticstr)
        # self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div').send_keys('\n')
        # time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div').send_keys(self.lottestr)
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div').send_keys('\n')
        # time.sleep(2)
        titles = self.driver.find_elements_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div/p')
        # titles.clear()
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / p[11]
        # print(str(len(self.driver.find_elements_by_css_selector('span.gOuterLink'))))
        # for text in self.driver.find_elements_by_css_selector('span.gOuterLink'):
        #     print(text.send_keys(''))
        # print(str(len(titles)))
        # for count in range(1,len(titles)):
        #     self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div/p['+str(count)+']').send_keys('')
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / p[1]
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / p[2]
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / p[3]
        print("완료")
        self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[4]/div/button').click()
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / div[1] / span / img
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / div[2] / span / img
        # self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]/div/p').send_keys('하이')
        # textfield = self.driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div/div/section/div/div/div/div[3]')
        # self.driver.execute_script("document.body.innerHTML = 'your contents'")
        # textfield.find_element_by_xpath('//*[@id="postWriteFormPlaceholderText"]').send_keys('하이')
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / p[2]
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / p[36] / span[1]
        # // *[ @ id = "wrap"] / div[2] / div / div / section / div / div / div / div[3] / div / p[37] / span[1]

        time.sleep(60)

    def fullpage_screenshot(driver, file):

        print("Starting chrome full page screenshot workaround ...")

        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return document.body.clientWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        print(
            "Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height, viewport_width, viewport_height))
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
                rectangles.append((ii, i, top_width, top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if not previous is None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)
                driver.execute_script(
                    "document.getElementById('topnav').setAttribute('style', 'position: absolute; top: 0px;');")
                time.sleep(0.2)
                print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)

            file_name = "part_{0}.png".format(part)
            print("Capturing {0} ...".format(file_name))

            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])

            print("Adding to stitched image with offset ({0}, {1})".format(offset[0], offset[1]))
            stitched_image.paste(screenshot, offset)

            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle

        stitched_image.save(file)
        print("Finishing chrome full page screenshot workaround...")
        return True


Encar_class(interval=60)
