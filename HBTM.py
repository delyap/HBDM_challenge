"""
    API Read of

    Create a vector of weights for the portfolio using mean-variance portfolio optimization. Using the
    conntracts available on HBDM from 2019-11-01T05:00:00+00:00 to 2019-
    11-15T23:00:00+00:00 using 1 hour data. Construct the portfolio using the following three contracts:
    BTC1227, XRP1227, LTC1227.

   Python 3 
"""

# Solve 'NameError: name 'requests' is not defined' by installing request module with "sudo apt-get install python3-requests"
import requests
#import time

# 请求行数据， Kline data

url = 'https://api.huobi.br.com/market/history/kline?period=60min&size=900&symbol=btcusdt'
resp = requests.get(url)
print(resp)
print(resp.json())
resp_json = resp.json()
print(resp_json['status'])
data_list = resp_json['data']
for data in data_list:
    print(data)
