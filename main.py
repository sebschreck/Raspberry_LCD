
# coding: utf-8

# In[6]:

import os
import requests
import time
import sched
import threading
from function_get_vvs import *
import lcddriver
import datetime

lcd = lcddriver.lcd()

U13,U14 = get_vvs_data()

update_display_vvs(U14,U13)






