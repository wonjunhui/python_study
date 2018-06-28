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


driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
driver.get('https://www.naver.com')
# time.sleep(2)
elem = driver.find_element_by_tag_name('body')
# elem.context_click()
elem.send_keys(Keys.COMMAND + 't')
# elem.send_keys(Keys.END)
# ActionChains(driver).key_down(Keys.COMMAND + 't')
actionChains = ActionChains(driver)
actionChains.context_click(elem).perform()

time.sleep(20)