import urllib.request, time, os, re, csv, sys

def fetch(daumticker):
    #print("daumticker",daumticker)
    url="http://finance.daum.net/item/main.daum?code="
    txt=urllib.request.urlopen(url+daumticker).read().decode()
    k=re.search('class="curPrice(.*?)">(.*?)<',txt)
    r=re.search('class="rate (.*?)?>(.*?)<',txt)
    if k:
        price=k.group(2)
        #q=tmp.replace(',','')
    else:
        price = "Nothing found for: " + daumticker + " price"
    if r:
        rate = r.group(2)
    else:
        rate = "Nothing found for: " + daumticker + " rate"
    return price, rate


# display time corresponding to your location
print(time.ctime())

# Set local time zone to Seoul
os.environ['TZ']='Asia/Seoul'
time.tzset()
t=time.localtime() # string
print(time.ctime())


def combine(ticker):
    price, rate = fetch(ticker)
    t=time.localtime()    
    output=[t.tm_year,t.tm_mon,t.tm_mday,t.tm_hour,  
            t.tm_min,t.tm_sec,ticker,price,rate]
    return output




tickers = ['234100']
for i in range(1,len(sys.argv)):
    tickers.append(sys.argv[i])

print("Stock List(s) : ",tickers)
# define the name of an output file


fname="portfolio.csv"
# remove a file, if exist
os.path.exists(fname) and os.remove(fname)

freq=1 



with open(fname,'a') as f:
    writer=csv.writer(f,dialect="excel") #,delimiter=" ")
    while(t.tm_hour<=15):
        if(t.tm_hour==15):
            while(t.tm_min<30):
                for ticker in tickers:
                    data=combine(ticker)
                    print(data)
                    writer.writerow(data)
                time.sleep(freq)
            else:
                break
        else:
            for ticker in tickers:
                data=combine(ticker)
                print(data)
                writer.writerow(data)
            time.sleep(freq)

f.close()