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
import multiprocessing as mp
from pytz import timezone
from socket import error as SocketError
import errno
# from pyvirtualdisplay import Display


class start_blog:
    def __init__(self):
        # sys.stdout.flush()
        self.data = []
        self.nowtime = ""
        self.totalstr = ""
        # self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
        # self.driver.implicitly_wait(3)
        self.keywords = []
        self.addresskeywords = []
        self.posts = []
        self.nowtime = datetime.now(timezone('Asia/Seoul')).strftime("%Y년 %m월 %d일 %H시%M분")
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-extensions')
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')

        # self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options)
        # self.driver = webdriver.Chrome('chromedriver', chrome_options=options)

        self.driver.implicitly_wait(5)
        # print("블로그 시작")
        try:
            self.login()
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise
            pass
        time.sleep(2)
        self.driver.close()
        self.driver.quit()


    def keyword_mining(self):
        self.driver.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')
        # driver.set_page_load_timeout(60)
        time.sleep(5)
        # time.sleep(10)
        keyword_list = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div/div[4]/div/div/ul')
        # keyword_list = keyword_list.find_elements_by_css_selector('ul.rank_list')
        keyword_list_1 = keyword_list.find_elements_by_css_selector('li.list')
        # print(keyword_list_1[0].text)
        for count in range(0, len(keyword_list_1)):
            # print(content)
            # count = str(count)
            # print(keyword_list_1[count].text)
            print(' '.join(keyword_list_1[count].text.split(" ")[1:]))
            self.addresskeywords.append(' '.join(keyword_list_1[count].text.split(" ")[1:]))
            self.keywords.append(keyword_list_1[count].text)
        # self.driver.close()
        time.sleep(1)
        # self.login()
        self.news_scraping()
        # // *[ @ id = "content"] / div / div[3] / div / div / div[4] / div / div / ul / li[2]
        # print(keyword_list.find_elements_by_css_selector('span.title'))
        # driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    def parse_blog(self):
        req = requests.get('https://datalab.naver.com/keyword/realtimeList.naver')
        html = req.text
        soup = bs(html, 'html.parser')
        my_titles = soup.find_all(class_='keyword_rank select_date')
        # print(soup.find_all(
        #     class_='sister'))  # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister brother" href="http://example.com/tillie" id="link3">Tillie</a>]
        print(soup)
        # data = {}
        # for title in my_titles:
        #     data[title.text] = title.get('href')
        #     print(title.text)

    def login(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        time.sleep(2)
        account = dict()
        with open("./naveraccount.txt", 'rt') as fp:
            data = fp.readlines()
            for d in data:
                d = d.split(" ")
                account[d[0]] = d[1]
            fp.close()
        self.driver.find_element_by_name('id').send_keys(account['id'])
        self.driver.find_element_by_name('pw').send_keys(account['pwd'])
        # 로그인 버튼을 눌러주자.
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        # self.driver.get('https://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage=1&groupId=0')

        self.driver.switch_to.window(self.driver.window_handles[0])  # 새창떴을때 제거하는 로직
        # self.driver.close(self.driver.window_handles[1])
        # self.driver.close()

        # self.driver.find_element_by_xpath('//*[@id="container"]/div/aside/div/div[1]/nav/a[2]').click()
        # self.driver.get('https://blog.naver.com/wnwjqpower')
        self.driver.get('http://cafe.naver.com/dieselmania')
        self.driver.find_element_by_xpath('//*[@id="cafe-info-data"]/ul/li[2]/p/a').click()
        self.driver.find_element_by_xpath('//*[@id="myActivityLink"]/a[1]').click()
        time.sleep(2)
        self.driver.switch_to_frame('cafe_main')
        self.driver.switch_to_frame('innerNetwork')
        tbody = self.driver.find_element_by_xpath('//*[@id="main-area"]/div[3]/table/tbody')
        tds = tbody.find_elements_by_css_selector('span')
        titles = []
        print("len:"+str(len(tds)))
        for str_2 in tds:
            if "디매" in str_2.text:
                titles.append(str_2)
                # print(str_2.text)
        print(titles[0].text+"vs"+titles[1].text)
        if titles[0].text==titles[1].text:
            titles[0].click()
            time.sleep(2)
            self.driver.switch_to_default_content()
            self.driver.switch_to_frame('cafe_main')
            post_code = self.driver.find_element_by_xpath('//*[@id="linkUrl"]').text.split('http://cafe.naver.com/dieselmania/')[1]

            self.driver.find_element_by_xpath('//*[@id="post_"'+post_code+'"]/div/div[1]/div[2]/table/tbody/tr/td[8]/a').click()
            print("삭제됨:"+self.driver.find_element_by_xpath('//*[@id="post_22270824"]/div/div[1]/div[1]/table/tbody/tr/td[1]/span'))

    def news_scraping(self):
        i = 0
        for keyword in self.addresskeywords:
            postarr = []

            try:
                self.driver.get('https://search.naver.com/search.naver?where=nexearch&query=' + keyword)
                news_list = self.driver.find_element_by_css_selector('div.news.section')
                news = news_list.find_elements_by_class_name('type01')
                # news= self.driver.find_element_by_xpath('//*[@id="main_pack"]/div[3]/ul')
                # li = news.find_elements_by_tag_name("li")
                # print(str(len(li)))
                # print(news)
                i = i + 1
                self.totalstr = self.totalstr + '' + '**검색어 ' + str(i) + '위: ' + keyword + '**\n'
                for te in news:
                    # dl = te.find_element_by_css_selector('dl')
                    dt = te.find_elements_by_css_selector('dt')
                    for title in dt:
                        print(title.text)
                        # print(title.find_element_by_css_selector('a').get_attribute('href'))
                        # self.posts.append(title.text+'\n'+title.find_element_by_css_selector('a').get_attribute('href'))
                        # self.posts.append(title.text+'\n')
                        postarr.append(title.text + '\n')
                        self.totalstr = self.totalstr + title.text + '\n'
                        # self.posts.append("------------------------------------")

                # time.sleep(3)
                self.totalstr = self.totalstr + '\n'
                self.posts.append(postarr)

            except Exception as e:
                print(str(e))
                self.posts.append('뉴스 없음.\n')

        self.login()


if __name__ == '__main__':
    p = mp.Process(target=start_blog)
    # run `worker` in a subprocess
    p.start()
    # make the main process wait for `worker` to end
    p.join()
    # all memory used by the subprocess will be freed to the OS
# start_blog()
# pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
# pool.map(news_scraping, keyword_mining,login) # pool에 일을 던져줍니다.
