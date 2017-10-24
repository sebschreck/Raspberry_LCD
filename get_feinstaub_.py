
# coding: utf-8

# In[1]:

import os
import requests
import threading
import datetime
import lcddriver


# In[3]:

# Bitcoin value
def get_feinstaub():
	P1,P2= [0,0,0],[0,0,0]
	sensoren = [609,4208]
	for sensor_id in sensoren:
	    try:
	        r = requests.get('http://api.luftdaten.info/v1/sensor/'+str(sensor_id))
	        r_json = r.json()
	        P1[sensoren.index(sensor_id)] = float(r_json[0]['sensordatavalues'][0]['value'])
	        P2[sensoren.index(sensor_id)] = float(r_json[0]['sensordatavalues'][1]['value'])
	    except:
	        continue
	        
	P2 = [x for x in P2 if x != 0]
	P1 = [x for x in P1 if x != 0]
	PM_2_5 = sum(P1)/len(P1)
	PM_10 = sum(P2)/len(P2)
	feinstaub_display = 'PM10 ' + str(round(PM_10,2)) + ' PM2.5 ' + str(round(PM_2_5,2))
	lcd.lcd_display_string('                    ', 3)
    lcd.lcd_display_string(feinstaub_display, 3)
    threading.Timer(300, get_feinstaub).start()











