import os
import pandas as pd
import numpy as np


pandf = pd.read_csv('./test10.csv')
# pandf['close'] = pandf['close'].str.split('.')


# convert nparray
test1_arr = pandf['date'].values[::-1]
test2_arr = pandf['close'].values[::-1]
arr3 = []
arr3.append(test1_arr)
arr3.append(test2_arr)
arr3 = np.array(arr3)
print(len(test1_arr))
nparr = [[0 for col in range(2)]for row in range(4453)]
# nparr.astype('float32')
print(arr3)