#-*- coding: utf-8 -*-

import csv
import pandas as pd

csvList = []

f = open('./test_1.csv', 'r')  # 현재 경로의 exam.csv를 연다.
csvReader = csv.reader(f)  # reader로 파일을 읽는다.

for i in csvReader:  # 한 행씩 돌면서 i[2]값 (3번째 컬럼)을 가져와서 리스트에 저장한다.
    text = i
    # a = text.split(",")
    # print(a)
    # print(text)
    if "0" in text[2]:
        sentence = ''.join(text[2].split())
        print(str(unicode(text[1]))+sentence)
        # text[0].encode("utf-8")
        csvList.append(text)
# f = open('./test_2.csv','w')
print(csvList)

pandasFrame = pd.DataFrame(csvList)
# pandasFrame.to_csv('test_2.csv')
# with open('./test_2.csv', 'r', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# f = open('./test_1.csv', 'r')  # 현재 경로의 exam.csv를 연다.
# csvWriter = csv.writer(f)
# csvWriter.writerow(csvList)
f.close()

