# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
import requests
import urllib.request
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from urllib.request import urlopen

image_list = []
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
driver.implicitly_wait(3)

driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Fpage.kakao.com%2Fstore%2Flogin%3FreturnUrl%3Dhttps%3A%2F%2Fpage.kakao.com')
driver.find_element_by_id('loginEmail').send_keys('kanz4861@gmail.com')
driver.find_element_by_id('loginPw').send_keys('tndk1101')
# driver.find_element_by_xpath('//*[@id="btn_login"]').click()
params = {
    'expires':'1522121205',
    'credential':'lUt9i42FY2I4ggejDuJPPXMt5QR0LkfX',
    'plink':'/home/47598147?categoryUid=10&subCategoryUid=1001&navi=1&inkatalk=0',
}
driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/button').click()
# time.sleep(30)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/span[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/ul/li[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
time.sleep(2)

page = requests.get(driver.current_url,params=params).text
page = driver.page_source
bs2 = BeautifulSoup(page,"lxml")

# print(bs2)

# print
# print(str(driver.current_url))
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
print(originSrc)
time.sleep(2)
actions = ActionChains(driver)
# print(actions)
actions.key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
cookies = driver.get_cookies()
driver.delete_all_cookies()
# print('cookies:'+cookies.text)
# for cookie in cookies:
#     print(cookie)
# trace_key=N_162126199536; L=1524126199907; page.kakako.com=GA1.3.1092458678.1524126200; page.kakako.com_gid=GA1.3.1288565969.1524126200; _gat=1
elem = driver.find_element_by_tag_name('html')
print(elem.text)
elem.send_keys(Keys.COMMAND + 't')
time.sleep(2)
print(originSrc[0]['value'])
print(originSrc[1]['value'])
print(originSrc[2]['value'])
outpath = '/Users/wonjunhui/Desktop'
# '/Users/wonjunhui/Desktop'
outfile = "testtete.png"
# urllib.request.urlretrieve(originSrc[0]['value'], outpath+outfile)
driver.get(originSrc[0]['value'])
# driver.find_element_by_tag_name('body').click()
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND, 's')
# driver.get(originSrc[0]['value'])
# ActionChains(driver).key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
# actions = ActionChains(driver)
# actions.key_down(Keys.COMMAND).send_keys('t').key_up(Keys.COMMAND).perform()
elem = driver.find_element_by_tag_name('html')
# print(elem.text)
elem.send_keys(Keys.COMMAND + 't')
# actionChains = ActionChains(driver)
# actionChains.context_click().perform()
# time.sleep(2)
# actionChains.key_down(Keys.ARROW_DOWN)
# actionChains.key_down(Keys.ARROW_DOWN)
# actionChains.key_down(Keys.ENTER)
# ActionChains(driver).key_down(Keys.CONTROL + 't')
# ActionChains(driver).key_down('t')
# actionChains = ActionChains(driver)
# q = driver.find_element_by_tag_name('body')
# q.send_keys(Keys.COMMAND)
# q.send_keys('t')
# data = urlopen(originSrc[0]['value'])
# soup = BeautifulSoup(data, 'html.parser')
# img = soup.find('img')
# q.send_keys(Keys.COMMAND, 't')
# actionChains.context_click(your_link).perform()
# ActionChains(driver).click('body',2).perform();
# f = open()
f = open(os.path.join(outpath, outfile), 'a')
# f.write(originSrc[0]['value'].read())
print("end")
time.sleep(100)
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


