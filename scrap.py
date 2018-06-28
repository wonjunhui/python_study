import pandas as pd 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from pandas_datareader import data

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0] # 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌 
code_df.종목코드 = code_df.종목코드.map('{:06d}'.format) # 우리가 필요한 것은 회사명과 종목코드이기 때문에 필요없는 column들은 제외해준다. 
code_df = code_df[['회사명', '종목코드']] # 한글로된 컬럼명을 영어로 바꿔준다. 
code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'}) 
code_df.head()
# print(code_df.head())

def get_url(item_name, code_df): 
    code = code_df.query("name=='{}'".format(item_name))['code'].to_string(index=False) 
    url = 'http://finance.naver.com/item/sise_day.nhn?code={code}'.format(code=code) 
    print("요청 URL = {}".format(url)) 
    return url # 신라젠의 일자데이터 url 가져오기 
item_name='대동기어'  
url = get_url(item_name, code_df) # 일자 데이터를 담을 df라는 DataFrame 정의 
df = pd.DataFrame()
html = urlopen(url)
source = BeautifulSoup(html.read(), "html.parser")
maxPage=source.find_all("table",align="center")
mp = maxPage[0].find_all("td",class_="pgRR")
mpNum = int(mp[0].a.get('href')[-3:])
 # 1페이지에서 20페이지의 데이터만 가져오기 
for page in range(1, mpNum+1): 
    pg_url = '{url}&page={page}'.format(url=url, page=page) 
    print(pd.read_html(pg_url, header=0))
    df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True) 

    df.to_csv('./testdaedong.csv'.format(pd.read_html(pg_url, header=0)[0]))

    # df.dropna()를 이용해 결측값 있는 행 제거 
    df = df.dropna() 
    
    # df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'}) 

# 한글로 된 컬럼명을 영어로 바꿔줌 
df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'}) 
# 데이터의 타입을 int형으로 바꿔줌 
df[['close', 'diff', 'open', 'high', 'low', 'volume']] \
   = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int) 
   # 컬럼명 'date'의 타입을 date로 바꿔줌 
df['date'] = pd.to_datetime(df['date']) 
   # 일자(date)를 기준으로 오름차순 정렬 
df = df.sort_values(by=['date'], ascending=True) 
   # 상위 5개 데이터 확인 
df.head()


