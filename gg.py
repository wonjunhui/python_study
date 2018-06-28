import bithumb
import time

count = 0
start = time.time()
while count <= 300:
	print(bithumb.bithumb.BTC,bithumb.coinone.XRP,bithumb.korbit.ETH) 
	# print(bithumb.coinone.XRP)
	# print(bithumb.korbit.ETH)
	time.sleep(1)
	count = count + 1
end = time.end()