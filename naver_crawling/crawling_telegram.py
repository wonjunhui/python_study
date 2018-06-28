# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
import time
import requests
import telegram

bot = telegram.Bot(token='485029394:AAEMIt1L0HkolhN-wpQ8aWLJh3J7zT-sNFk')
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# while True:
# 	try:
# 		req = requests.get('http://finance.naver.com/item/board_read.nhn?code=007460&nid=78742140')
# 		req.encoding = 'utf-8'
# 		html = req.text
# 		soup = BeautifulSoup(html, 'html.parser')
# 		posts = soup.find("em",{"class": "no_down"})
# 		post = posts.find("span",{"class": "blind"})
# 		post = post.text
# 		print(post)
# 			# time.sleep(3)
# 		latest = post
# 		print("0")
# 		f_read = (os.path.join(BASE_DIR, 'latest.txt'), 'r+')
# 		before = f_read.readline()
# 		print("1")
# 		if before != latest:
# 	            # for x in range(len(list)):
# 			bot.sendMessage(chat_id=chat_id, text=post)
# 			print("2")
# 		else:
# 			bot.sendMessage(chat_id=chat_id, text="")
# 			print("3")

# 		f_read.close()
# 		print("4")
	    
# 		with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
# 			f_write.write(latest)
# 			f_write.close()
# 			time.sleep(3) # 60초(1분)을 쉬어줍니다.
# 	except:
# 		print("오류")
# 		time.sleep(3) # 60초(1분)을 쉬어줍니다.



while True:
	try:
		req = requests.get('http://finance.naver.com/item/main.nhn?code=234100')
		req.encoding = 'utf-8'
		rate = ""
		html = req.text
		soup = BeautifulSoup(html, 'html.parser')
		div_class = soup.find("p",{"class": "no_today"})
		try:
			posts = div_class.find("span","blind")
		except FileNotFoundError as e:
			print(str(e))
			posts = div_class.find("span","blind")
		print(posts.text)
		# post = posts.find("span",{"class": "blind"})
		post = posts.text
		post = post.replace(',','')
		# post =post.split('\n')[1] 
		# # print(post.split('\n')[1])
		# print(post)

		now = time.localtime()

		s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

		latest = post
		# print(latest)
		# print('post:'+post)
		with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
			before = f_read.readline()
			if before > latest:
	            # for x in range(len(list)):
				bot.sendMessage(chat_id=chat_id, text=post+"원")
				print(s)
				print("변동있음------------------------")


			else:
				# bot.sendMessage(chat_id=chat_id, text="나는 바보야")
				print(s)
				print("변동없음")
			f_read.close()
	    
		with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
			f_write.write(latest)
			f_write.close()
	    
		time.sleep(1) # 60초(1분)을 쉬어줍니다.

	except FileNotFoundError as e:
		print("오류"+str(e))
		time.sleep(3) # 60초(1분)을 쉬어줍니다.