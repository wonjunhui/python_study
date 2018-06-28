# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
from urllib.request import urlopen
import requests

req = requests.get('https://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage=1&groupId=0').text
soup = BeautifulSoup(req,'html.parser')
print(soup)