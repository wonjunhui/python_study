import pandas as pd
import numpy as np
import os

df = pd.read_csv('./testdaedong.csv')
df = df.rename(columns= {'날짜': 'date', '종가': 'close', '전일비': 'diff', '시가': 'open', '고가': 'high', '저가': 'low', '거래량': 'volume'}) 
# 데이터의 타입을 int형으로 바꿔줌 
df[['close', 'diff', 'open', 'high', 'low', 'volume']] \
   = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int) 
   # 컬럼명 'date'의 타입을 date로 바꿔줌 
df['date'] = pd.to_datetime(df['date']) 
   # 일자(date)를 기준으로 오름차순 정렬 
df = df.sort_values(by=['date'], ascending=False) 
df = df[['date','close']]
# df = pd.DataFrame(df.values);
df.to_csv('./testdaedong.csv')

   # 상위 5개 데이터 확인 
# df.head()



# nparr = pandf['Close'].values[::-1]
# nparr.astype('float32')
print(df)
