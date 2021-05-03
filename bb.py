import pyupbit 
import time
import pprint
access "D6HyQn7eNSRG7xrgxVs3LucaBY2xyPXnNho25nHd"
secret "n8xgTAK9MRCqdQxVG12GIfwcZurmW20T0sLYx9zd"
upbit =pyupbit.upbit(access, secret)

while True:
   eth = pyupbit.get_chlcv( "krw-ETH","minute1") 
   close = eth['close']
   window100 = close.rolling(100)
   ma100 = window100.mean()
   last_ma100 = ma100[199]
   last_close = close(199) 
   last_trend = last_close - last_ma100
   check_trend = check_close - check_ma100
   balance = upbit.get balance("KRw-ETH") 
   abp=upbit.get_avg_buy_price("krw-eth")
   max_margin = 100

   if last trend > 0 :
      if check trend <= 0 :
          if balance <= 0 :
            buy_record = upbit.buy_market_order("krw-eth" , 10000")
            print(time.strftime('%y-%m-%d %h:%m:%s'),"close:", last_close, "ma100:", last_ma100," ", round (last_trend), "", "abp", abe, " " "balance:", balance, "BUY")

   if balance > 0 :('%y-%m-%d %h:%m:%s'),"close:", last_close, "ma100:", last_ma100," ", round (last_trend), "", "abp", abe, " " "balance:", balance, "hold")

   if check trende > 0 :
       if balance <= 0 :
          print(time.strftime('%y-%m-%d %h:%m:%s'),"close:", last_close, "ma100:", last_ma100," ", round (last_trend), "", "abp", abe, " " "balance:", balance, "BUY TIMING CHECK")
       if balance > 0 :
          print(time.strftime('%y-%m-%d %h:%m:%s'),"close:", last_close, "ma100:", last_ma100," ", round (last_trend), "", "abp", abe, " " "balance:", balance, "hold")
 
if last_trend <= 0:     
    if balance > 0:
      sell_record upbit.sell_market order ( "krw-eth" , balance)
      pprint.pprint(sell_record) 
      print(time.strftime('%y-%m-%d %h:%m:%s'),"close:", last_close, "ma100:", last_ma100," ", round (last_trend), "", "abp", abe, " " "balance:", balance, "sell")
      
    if balance <=0:
      print(time.strftime('%y-%m-%d %h:%m:%s'),"close:", last_close, "ma100:", last_ma100," ", round (last_trend), "", "abp", abe, " " "balance:", balance, "sell") 

if abp > 0 :
   margin = (last_close - abp)/abp 
   print("margin:", round(margin, 4))

time.sleep(60)
