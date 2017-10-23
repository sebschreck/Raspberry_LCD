
# coding: utf-8

# In[6]:

import os
import requests
import time
import sched
import threading
from function_get_vvs import *
from get_other_stuff import *
import lcddriver
import datetime

lcd = lcddriver.lcd()

U14,U13 = get_vvs_data()
update_display_vvs(U14,U13,lcd)
get_bitcoin_value(lcd)





