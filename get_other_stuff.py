
# coding: utf-8

# In[1]:

import os
import requests
import threading
import datetime
#import lcddriver


# In[3]:

# Bitcoin value
def get_bitcoin_value(lcd):
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dataframe = r.json()
    BTC_string = 'BTC: 'dataframe['bpi']['USD']['rate'][:5] + '$'
    lcd.lcd_display_string(BTC_string, 2)
    threading.Timer(3600, get_bitcoin_value, [lcd]).start()


# In[8]:




# In[12]:



