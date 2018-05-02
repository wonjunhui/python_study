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
        self.nowtime = datetime.now(timezone('Asia/Seoul')).strftime("%Y년 %m월 %d일 %H시")
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-extensions')

        # self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options)
        # self.driver = webdriver.Chrome('chromedriver', chrome_options=options)
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver',chrome_options=options)

        self.driver.implicitly_wait(5)
        print("블로그 시작")
        try:
            self.Most_view()
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise
            pass
        time.sleep(2)
        self.driver.close()
        self.driver.quit()
        # self.driver.close()
        # self.keyword_mining()

        # while True:
        #     self.nowtime = datetime.now().strftime("%Y년 %m월 %d일 %H시%M분")
        #     ntime = datetime.now().strftime("%Y년 %m월 %d일 %H시%M분%S초")
        #     # print(now[-4:])
        #     print(ntime)
        #     now = datetime.now().strftime("%H%M%S")

        #     if now[-4:] == "0000" or now[-4:] == "3000":
        #         print("현재시간 : "+now)
        #         options = webdriver.ChromeOptions()
        #         options.add_argument('--disable-extensions')
        #         options.add_argument('headless')
        #         options.add_argument('window-size=1920x1080')
        #         options.add_argument("disable-gpu")
        #         options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        #         options.add_argument('--no-sandbox')
        #         self.driver = webdriver.Chrome('chromedriver', chrome_options=options)
        #         self.driver.implicitly_wait(3)
        #         self.keyword_mining()
        #         time.sleep(60)
        #     time.sleep(1)

    def Most_view(self):
        print("----------현재 인기 뉴스----------")
        self.driver.get('http://sports.news.naver.com/wfootball/news/index.nhn')
        rank_news = self.driver.find_element_by_xpath('//*[@id="rankingNewsList_0"]')
        rank_news_li = rank_news.find_elements_by_css_selector('li')
        # rank_news_a = rank_news.find_elements_by_css_selector('a')
        self.totalstr = "------현재 인기 뉴스------"
        for news in rank_news_li:
            news_a = news.find_element_by_css_selector('a')
            # self.domesticstr= self.domesticstr + '\n' + news.text + '\n' +news_a.get_attribute("href")
            self.totalstr = self.totalstr + '\n' + news_a.get_attribute("href")
            self.data.append(news_a.get_attribute("href"))
            print(news.text)
        time.sleep(2)
        self.login()


    def login(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        time.sleep(2)
        self.driver.find_element_by_name('id').send_keys('wnwjqpower')
        self.driver.find_element_by_name('pw').send_keys('wnsgml!59')
        # 로그인 버튼을 눌러주자.
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.get('https://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage=1&groupId=0')

        self.driver.switch_to.window(self.driver.window_handles[0])  # 새창떴을때 제거하는 로직
        # self.driver.close(self.driver.window_handles[1])
        # self.driver.close()

        # self.driver.find_element_by_xpath('//*[@id="container"]/div/aside/div/div[1]/nav/a[2]').click()
        self.driver.get('https://blog.naver.com/wnwjqpower')

        time.sleep(2)
        self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.
        self.driver.find_element_by_xpath('//*[@id="category13"]').click()
        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="post-admin"]/a[1]').click()
        self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.
        confirm = self.driver.find_element_by_id('btn_submit')
        title = self.driver.find_element_by_name('post.title')
        title.click()
        title.send_keys(self.nowtime + " 해외축구 인기뉴스")
        time.sleep(5)
        self.driver.switch_to.frame('se2_iframe')
        index = self.driver.find_element_by_class_name('se2_inputarea')
        # for count in range(0,len(self.posts)):
        #     self.driver.switch_to_default_content()
        #     self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.
        #     self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[1]/li[2]/button').click() # 글자크기 변경
        #     time.sleep(1)
        #     self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[1]/li[2]/div/div/ul/li[6]/button').click() # 글자크기 변경 (12pt)
        #     # time.sleep(1)
        #     self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[2]/li[5]/span[3]/button').click() # 글자색 변경
        #     time.sleep(1)
        #     self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[2]/li[5]/div/div/div/ul[1]/li[10]/button').click() # 글자색 변경 (보라색)
        #     # time.sleep(1)
        #     self.driver.switch_to.frame('se2_iframe')
        #     index = self.driver.find_element_by_class_name('se2_inputarea')
        #     index.send_keys('검색어 '+str(count+1)+'위: '+' '.join(self.keywords[count].split(' ')[1:]) + '\n')

        #     self.driver.switch_to_default_content()
        #     self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.
        #     self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[1]/li[2]/button').click()  # 글자크기 변경
        #     time.sleep(1)
        #     self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[1]/li[2]/div/div/ul/li[4]/button').click()  # 글자크기 변경 (10pt)
        #     # time.sleep(1)
        #     self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[2]/li[5]/span[3]/button').click()  # 글자색 변경
        #     time.sleep(1)
        #     self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[2]/li[5]/div/div/div/ul[2]/li[19]/button').click()  # 글자색 변경 (shftor)
        #     # time.sleep(1)
        #     self.driver.switch_to.frame('se2_iframe')
        #     index = self.driver.find_element_by_class_name('se2_inputarea')
        #     index.send_keys(''.join(self.posts[count]))
        #     index.send_keys('\n')
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.
        # self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[1]/li[2]/button').click() # 글자크기 변경
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[1]/li[2]/div/div/ul/li[6]/button').click() # 글자크기 변경 (12pt)
        #     # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[2]/li[5]/span[3]/button').click() # 글자색 변경
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[2]/li[5]/div/div/div/ul[1]/li[10]/button').click() # 글자색 변경 (보라색)
        # time.sleep(1)
        self.driver.switch_to.frame('se2_iframe')
        index = self.driver.find_element_by_class_name('se2_inputarea')
        # index.send_keys('검색어 '+str(count+1)+'위: '+' '.join(self.keywords[count].split(' ')[1:]) + '\n')

        # self.driver.switch_to_default_content()
        # self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.
        # self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[1]/li[2]/button').click()  # 글자크기 변경
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[1]/li[2]/div/div/ul/li[4]/button').click()  # 글자크기 변경 (10pt)
        #     # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[2]/li[5]/span[3]/button').click()  # 글자색 변경
        # time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[2]/li[5]/div/div/div/ul[2]/li[19]/button').click()  # 글자색 변경 (shftor)
        #     # time.sleep(1)
        # self.driver.switch_to.frame('se2_iframe')
        # index = self.driver.find_element_by_class_name('se2_inputarea')
        for text in self.data:
            index.send_keys(text+'\n')
            time.sleep(3)
        # index.send_keys(self.totalstr)
        # index.send_keys('\n')
        # text_token = twitter.nouns(count)
        # pprint(twitter.nouns(text_token))
        # counter = Counter(text_token)
        # time.sleep(10)

        print("성공")
        self.driver.switch_to_default_content()
        self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.
        # self.driver.find_element_by_xpath('//*[@id="set_close"]').click()
        confirm.click()

        # time.sleep(5)

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
        # req = requests.get('https://search.naver.com/search.naver?where=nexearch&query=%EB%B6%80%EC%9E%A3%EC%A7%91%20%EC%95%84%EB%93%A4')
        # html = req.text
        # soup = bs(html, 'html.parser')
        # my_titles = soup.find_all(class_='news section')
        # print(soup)


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
