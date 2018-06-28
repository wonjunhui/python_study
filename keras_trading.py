import os
import pandas as pd
import numpy as np
import pandas as pd 
from pandas import Series, DataFrame
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import LSTM
# from sklearn.preprocessing import MinMaxScaler
# import matplotlib.pyplot as plt
# import math
# from sklearn.metrics import mean_squared_error
 
look_back = 1
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i + look_back)]
        dataX.append(a)
        dataY.append(dataset[i + look_back])
    return np.array(dataX), np.array(dataY)
 
# file loader

pandf = pd.read_csv('./testsam.csv')
 
# convert nparray
arr1 = pandf['close'].values[::-1]
arr2 = pandf[['date','close']]
arr3 = []
for i in range(len(arr2)) :
	a = arr2['date'].iloc[i]
	if '2017' in arr2['date'].iloc[i] or '2018' in arr2['date'].iloc[i]:
		arr3.append(arr2.values[i])
		# print(arr2.values[i])

arr3 = DataFrame(arr3)
arr3.rename(columns={arr3.columns[0]:"date",arr3.columns[1]:"close"}, inplace = True)
arr3 = arr3['close']
# print(arr3)
	# print(a)
# print(arr2)
arr3.to_csv('./20172018_data.csv', index = False)
# arr2 = pandf['date'].values[::-1]
# arr3 = []
# for i in range(len(arr2)):
# 	a = arr2[i]
# 	a = a.replace("-","")
# 	arr3.append(a)
# # print(arr3)
# nparr = []
# nparr.append(arr1)
# nparr.append(arr3)
# nparr = np.array(nparr)
# nparr.tolist()
# # nparr.astype('float32')
# # print(nparr)
#  