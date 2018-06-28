from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException

# driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
# driver.implicitly_wait(3)

# driver.get("https://www.naver.com")


# driver.find_element_by_name("query").send_keys("부산 날씨")
# driver.find_element_by_id("search_btn").click()

account = dict()
list_out = []
ex_list = []
text_list = []
# time.sleep(10)


fp = open("./total_car_list.txt", 'rt')
data = fp.readlines()
# print(data[0])
	# fp.close()
for d in data:
   	d = d.split("|")
   	d2 = d[0].split("(")
   	d2 = d2[0].split(" ")
   	ex_list.append(d[2]+" "+d2[0])
   	# print(d[2]+""+d2[0])
   	list_out.append({'name': d[0], 'car_fuel': d[1], 'car_brand_name': d[2], 'car_type':" "})

ex_list = list(set(ex_list))
try:
	for i in range(0,len(ex_list)):
		if i+1 < len(ex_list):
			# print(ex_list[i+1]+" vs "+ex_list[i].split(" ")[1])
			for j in range(0,len(ex_list)):
				print(ex_list[j]+" vs "+ex_list[i].split(" ")[1])
				if ex_list[j] in ex_list[i].split(" ")[1] :
					f = open('cartype_list.txt', 'a')
					f.write(ex.list[i]+'\n')
					f.close()
				# print(ex_list[i])
					ex_list.pop(j)
				
except FileNotFoundError as e:
	print("gd"+str(e))
# print(ex_list)
# pandasFrame = pd.DataFrame(list_out)
# pandasFrame.to_csv('total_1.csv')
fp.close()
  #       d = d.split("|")
		# # 		# account[d[0]] = d[1]
		# print(d)
	# print(data[0])
 #    fp.close()
