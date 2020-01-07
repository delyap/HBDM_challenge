"""

Error Resolving Log:
https://docs.google.com/document/d/1pAwvzIF5XRqaDfaU_S4BBH3GHT1Y8tttfzU6LdKeBKE/edit?usp=sharing

Python 3
   
"""

# Install requests: "sudo apt-get install python3-requests" (Linux)
## Install requests: apt-get install python3-requests (Windows in Administrative Cmd Prompt)
# Install pandas: pip install pandas

import requests             ##get module in Python
import pandas as pd         ##view data in clean manner 
pd.set_option('expand_frame_repr', False)        ##expand .. columns in output, comment to remove

pd.set_option('display.max_rows', 1000)

# Kline data

url_btc  = 'https://api.huobi.br.com/market/history/kline?period=60min&size=1&symbol=btcusdt'
url_xrp = 'https://api.huobi.br.com/market/history/kline?period=60min&size=1&symbol=xrpusdt'
url_ltc = 'https://api.huobi.br.com/market/history/kline?period=60min&size=1&symbol=ltcusdt'

#resp = requests.get('https://api.huobi.br.com/market/history/kline?period=60min&size=2&symbol=btcusdt')

resp_btc = requests.get(url_btc, auth=('user', 'pass'))         ##standard get command to GET data
resp_btc_json = resp_btc.json()                                 ##resp = requests.get(url).json()

resp_xrp = requests.get(url_xrp, auth=('user', 'pass'))         ##standard get command to GET data
resp_xrp_json = resp_xrp.json()                                 ##resp = requests.get(url).json()

resp_ltc = requests.get(url_ltc, auth=('user', 'pass'))         ##standard get command to GET data
resp_ltc_json = resp_ltc.json()                                 ##resp = requests.get(url).json()

##print(resp.status_code)
##print(resp.headers['content-type'])
##print(resp.encoding)
##print(resp.text)

##r_json = resp.json()                ##standard get command

##print(resp)
##print(resp.json()['status'])           ##print list of status

##print('btc')
##print(requests.get(url_btc, auth=('user', 'pass')).json()['data'])           ##print list of data under btc
##
##print('')
##print('xrp')
##print(requests.get(url_xrp, auth=('user', 'pass')).json()['data'])           ##print list of data
##
##print('')
##print('ltc')
##print(requests.get(url_ltc, auth=('user', 'pass')).json()['data'])           ##print list of data

print('This is the Data Table for BTC')
data_list_btc = resp_btc_json['data']       ##requests.get(url).json() -> data column
df_btc = pd.DataFrame(data_list_btc)        ##cleaner data output
print(df_btc)                               ##print data table for BTC
print('--'*40)                                   ##aesthetically pleasing to eye
print('')                                   ##aesthetically pleasing to eye

print('This is the Data Table for XRP')
data_list_xrp = resp_xrp_json['data']       ##requests.get(url).json() -> data column
df_xrp = pd.DataFrame(data_list_xrp)        ##cleaner data output
print(df_xrp)                               ##print data table for XRP
print('--'*40)                                   ##aesthetically pleasing to eye
print('')                                   ##aesthetically pleasing to eye

print('This is the Data Table for LTC')
data_list_ltc = resp_btc_json['data']       ##requests.get(url).json() -> data column
df_ltc = pd.DataFrame(data_list_ltc)        ##cleaner data output
print(df_ltc)                               ##print data tablefor LTC
print('--'*40)                                   ##aesthetically pleasing to eye
print('')                                   ##aesthetically pleasing to eye


##symbol = 'ethusdt'
###https://api.huobi.br.com/market/detail/merged?symbol=ethusdt
##test_url = 'https://api.huobi.br.com' + '/market/detail/merged' + '?' + 'symbol=' + symbol
##print('test url is: \n' + test_url)
##resp_test_url = requests.get(test_url)           ##usual get command
##print(resp_test_url.json() )
##print('--'*40)                                   ##aesthetically pleasing to eye
##print(resp_test_url.json()['tick'])
##print(pd.DataFrame(resp_test_url.json()))
##
##
##
####ticker = resp_test_url.json()['tick']
####print('Selling Price is :' + str(ticker['ask']))
####print('Buying Price is :' + str(ticker['bid']))
##
##
##
##ticker = resp_test_url.json()['tick']
##print('--'*40)                                   ##aesthetically pleasing to eye
##print('Selling Price is : ' , str(ticker['ask'][0]))
##print('Buying Price is : ' , str(ticker['bid'][0]))



##data = resp.json()['data']
##for d in data:                    ##print seperate blocks of data
##    print(d)


##print(resp.json()['data'][2])



##resp_json = resp.json()
##data_list = resp_json['data']
##for data in data_list:
##    print(data)

