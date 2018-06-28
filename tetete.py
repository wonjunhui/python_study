import pickle
import pandas as pd
# kosdaq = pickle.load(open('./kosdaq.pickle')) 
kosdaq2 = pd.read_pickle('kosdaq.pickle')
# kospi = pickle.load(open('./kospi.pickle')) 

kosdaq2.head()
print(kosdaq2)