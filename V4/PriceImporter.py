import yfinance as yf
import time


data=open("dat2a.txt",'w')
data.write("")
data.close()



for x in range(200):
    data=open("dat2a.txt",'a')
    YData=yf.Ticker("ETH-USD").info
    data.write("{}\n".format(YData["regularMarketPrice"]))
    data.close()
    time.sleep(1)
    print("Loaded")
data.close()
