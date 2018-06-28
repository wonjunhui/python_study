from pandas_datareader import data
import fix_yahoo_finance as yf
yf.pdr_override()
import pickle
import re
import pandas as pd
import glob
kosdaq = pd.read_pickle('kosdaq.pickle')
kospi = pd.read_pickle('kospi.pickle')
print(kosdaq)
# kospi = pickle.load(open('./kospi.pickle',encoding='UTF8'))
# kosdaq = open('kosdaq.pickle')

def save_kosdaq():
    for stock in kosdaq.values:
        kor_name = stock[0]
        ticker = stock[1]
        df = data.get_data_yahoo(ticker + '.KQ', '1996-05-06', thread=20)
        df.to_csv('./kosdaq/{}.csv'.format(ticker))
        print('{}.csv is saved'.format(ticker))

def save_kospi():
    for stock in kospi.values:
        kor_name = stock[0]
        ticker = stock[1]
        df = data.get_data_yahoo(ticker + '.KS', '1996-05-06', thread=20)
        df.to_csv('./kospi/{}.csv'.format(ticker))
        print('{}.csv is saved'.format(ticker))

save_kosdaq()
save_kospi()

def reload_empty(market):
    file_list = glob.glob('./{}/*.csv'.format(market))
    six_digit = re.compile('\d{6}')
    for file_name in file_list:
        file = pd.read_csv(file_name)
        if file.empty:
            print("empty file {} is updated".format(file_name))
            ticker = six_digit.findall(file_name)[0]
            _ticker = ticker + ['.KQ', '.KS']['market'=='kospi']
            tmp_df = data.get_data_yahoo(_ticker, start='1996-05-06', thread=20)
            
            tmp_df.to_csv(file_name)

reload_empty('kosdaq')
reload_empty('kospi')