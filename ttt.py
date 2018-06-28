import pandas as pd
import numpy as np
import os

df = pd.read_csv('./testdaedong.csv')
df.to_csv('./testdaedong.csv', index = False, header = False)
