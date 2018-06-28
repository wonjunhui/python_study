from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == "__main__":
 # 크롤링을 하려는 URL
 targetUrl = "http://aqicn.org/city/seoul/kr/"
 # 웹페이지를 읽어온다.
 html = urlopen(targetUrl).read()
 # beautifulsoup 으로 파싱
 soupData = BeautifulSoup(html, 'html.parser')
 # 지역 정보를 읽어 오고.
 titleData = soupData.find('a', id='aqiwgttitle1')
 print(titleData.string)