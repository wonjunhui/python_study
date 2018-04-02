# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
import requests


image_list = []
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver',chrome_options=options)
driver.implicitly_wait(3)

driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Fpage.kakao.com%2Fstore%2Flogin%3FreturnUrl%3Dhttps%3A%2F%2Fpage.kakao.com')
driver.find_element_by_id('email').send_keys('wnwjqpower@naver.com')
driver.find_element_by_id('password').send_keys('wns159')
driver.find_element_by_xpath('//*[@id="btn_login"]').click()
driver.get('https://page.kakao.com/home/47598147?categoryUid=10&subCategoryUid=1001&navi=1&inkatalk=0&inChannel=0')
driver.get('https://page.kakao.com/viewer?productId=47598360&categoryUid=10&subCategoryUid=1001&navi=1&inkatalk=0&inChannel=0')
driver.find_element_by_xpath('/html/body/div[4]/img').click()
params = {
    'expires':'1522121205',
    'credential':'lUt9i42FY2I4ggejDuJPPXMt5QR0LkfX',
    'plink':'/home/47598147?categoryUid=10&subCategoryUid=1001&navi=1&inkatalk=0',
}
page_source = requests.get('https://page.kakao.com/viewer?productId=47598360&categoryUid=10&subCategoryUid=1001&navi=1&inkatalk=0&inChannel=0',params=params).text
page_source = driver.page_source
bs = BeautifulSoup(page_source, "lxml")
# print(bs)
originSrc = bs.findAll("input",{"class":"originSrc"})
print(originSrc[0]['value'])
print(originSrc[1]['value'])
print(originSrc[2]['value'])

# count = driver.find_element_by_xpath('/html/body/div[2]/span').text
# count = count.split('/')[1].replace(" ","")
# for i in range(0,int(count)):
#     driver.find_element_by_xpath('/html/body/div[2]/div[2]/img').click()
#     print(str(i))
#     time.sleep(1)
#     image = driver.find_element_by_id('screen_'+str(i))
#     image_src = image.get_attribute('data-src')
#     image_list.append(image_src+'\n')

# driver.get(image_list[0])
# print(image_list[0])
# print(image_list[1])
# # driver.get(image_src)
# time.sleep(10)

# https://page-edge.kakao.com/sdownload/resource?kid=zPUDLFS_c58DrjIKOlfKL6WT-4GZ-Ln21Qv-5qmO6XI2-ayx3IrPgLr1BZf1l99p&filename=img_00001.jpg&signature=IT339gKJCTcogsSGzMLijK0oBmI%3D&expires=1522119018&credential=lUt9i42FY2I4ggejDuJPPXMt5QR0LkfX