import requests
from bs4 import BeautifulSoup

# Session 생성
s = requests.Session()

# HTTP GET Request: requests대신 s 객체를 사용한다.
req = s.get('http://finance.naver.com/sise/sise_low_up.nhn')

# HTML 소스 가져오기
html = req.text
# HTTP Header 가져오기
header = req.headers
# HTTP Status 가져오기 (200: 정상)
status = req.status_code
# HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok
# print(html)
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'td > a'
    )
for title in my_titles:
    # Tag안의 텍스트
    print(title.text)
    # Tag의 속성을 가져오기(ex: href속성)
    # print(title.get('href'))
    # contentarea > div.box_type_l > table > tbody > tr:nth-child(3)