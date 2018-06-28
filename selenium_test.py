# from selenium import webdriver
# driver = webdriver.Chrome("/Users/wonjunhui/Downloads/chromedriver")
# driver.get("http://www.google.co.kr")
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("Selenium")
# elem.submit()
# assert "No results found." not in driver.page_source
# driver.close()

import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ff_driver = webdriver.Chrome("/Users/wonjunhui/Downloads/chromedriver")
ff_driver.get("https://www.google.co.kr")

query = ff_driver.find_element_by_id("lst-ib").send_keys("macbook pro")
ff_driver.find_element_by_name("btnK").click()

WebDriverWait(ff_driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.r")))

page_results = ff_driver.find_elements(By.CSS_SELECTOR, "h3.r")

for item in page_results:
    print(item.text)