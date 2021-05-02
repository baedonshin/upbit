
import pyupbit

access = "DEytALjLVlWcs5L6ZIIysbgSCCYyc6qhxrTBb8AM"          # 본인 값으로 변경
secret = "VTNKeyTHRnvkfR6Yx6l8vHAhIGdl8GoF4qmnWAPu"          # 본인 값으로 변경
upbit =pyupbit. Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회






import pandas as pd
import datetime
import requests
import time
import webbrowser
import numpy as np

a = 1

while True:
    def goldencross(symbol):
        url = "https://api.upbit.com/v1/candles/minutes/5"
        
        querystring = {"market":symbol,"count":"100"}
        
        response = requests.request("GET", url, params=querystring)
        
        data = response.json()
        
        df = pd.DataFrame(data)
        
        df=df['trade_price'].iloc[::-1]
        
    
        global a
        if a==1:
 
            url = "https://bit.ly/3oWaIXG"
            webbrowser.open(url)
    
            url = "https://www.xn-----bt9ig0b31lcsga13i850awk2a6pg.com/"
            webbrowser.open(url)
            
            url = "https://www.binance.com/kr/register?ref=X1401JUS"
            webbrowser.open(url)            
            a=2    
        
    
        ma5 = df.rolling(window=5).mean()
        ma20 = df.rolling(window=20).mean()
        
        test1=ma5.iloc[-2]-ma20.iloc[-2]
        test2=ma5.iloc[-1]-ma20.iloc[-1]
        
        call='해당없음'
        
        if test1>0 and test2<0:
            pyupbit.buy_market_order("KRW-XRP", 10000)
            print("매수")
        if test1<0 and test2>0:
             pyupbit.sell_market_order("KRW-XRP", 10000)
             print("매도")
           
           
        
        print(symbol)
        print('이동평균선 5: ', round(ma5.iloc[-1],2))
        print('이동평균선 20: ', round(ma20.iloc[-1],2))
        print('골든크로스/데드크로스: ',call)
        print('')
        time.sleep(1)
    
    
    goldencross('KRW-XRP')
# [출처] 2021년 UPBIT 업비트 여러 종목 골든크로스 데드크로스 장기이동평균선 단기이동평균선  비트코인  표시해주는 파이썬 코드 (자동매매)|작성자 비트체인지

