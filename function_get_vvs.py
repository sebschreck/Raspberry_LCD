
# coding: utf-8

# In[22]:

import os
import requests
import threading
import datetime
import lcddriver

# In[21]:

def get_vvs_data():
    r = requests.get("https://efa-api.asw.io/api/v1/station/5006253/departures/?format=json")
    dataframe = r.json()
    Heslach_abfahrten = [0,0]
    Hedelfingen_abfahrten = [0,0]
    Heslach_counter = 0
    Hedelfingen_counter = 0
    for i in range(0,len(dataframe)):
        if ((dataframe[i]['direction']=='Heslach') & (dataframe[i]['number']=='U14') & (Heslach_counter<2) ):
            Heslach_abfahrten[Heslach_counter] = [dataframe[i]['departureTime'],dataframe[i]['delay']]
            Heslach_counter +=1
        if ((dataframe[i]['direction']=='Hedelfingen') & (dataframe[i]['number']=='U13')& (Hedelfingen_counter<2)):
            Hedelfingen_abfahrten[Hedelfingen_counter] = [dataframe[i]['departureTime'],dataframe[i]['delay']]
            Hedelfingen_counter +=1
        if (Hedelfingen_counter==2 & Heslach_counter==2):
            break
    threading.Timer(60, get_vvs_data).start()
    print('abfrage')
    return Heslach_abfahrten, Hedelfingen_abfahrten


def update_display_vvs(U14,U13,lcd):
    now = datetime.datetime.now()
    Minute_now = now.hour*60+now.minute+now.second/60

    U14_minute_next = (int(U14[0][0]['hour'])*60+int(U14[0][0]['minute'])+int(U14[0][1])-Minute_now)
    U13_minute_next = (int(U13[0][0]['hour'])*60+int(U13[0][0]['minute'])+int(U13[0][1])-Minute_now)
    if U14_minute_next<=4:
        U14_minute_next = (int(U14[1][0]['hour'])*60+int(U14[1][0]['minute'])+int(U14[1][1])-Minute_now) 
    if U13_minute_next<=4:
        U13_minute_next = (int(U13[1][0]['hour'])*60+int(U13[1][0]['minute'])+int(U13[1][1])-Minute_now) 

    seconds_U14 = str((int(U14_minute_next%1*60)))
    if len(seconds_U14)==1:
        seconds_U14 = '0' + str(seconds_U14)

    U14_display_string = 'U14 '+str(int(U14_minute_next//1))+':'+ seconds_U14

    seconds_U13 = str((int(U13_minute_next%1*60)))
    if len(seconds_U13)==1:
        seconds_U13 = '0' + str(seconds_U13)

    U13_display_string = 'U13 '+str(int(U13_minute_next//1))+':'+ seconds_U13
    print(datetime.datetime.now())
    print(U14_display_string)
    print(U13_display_string)
    lcd.lcd_display_string(U14_display_string+' '+U13_display_string, 1)
    threading.Timer(4, update_display_vvs, [U14,U13,lcd]).start()



