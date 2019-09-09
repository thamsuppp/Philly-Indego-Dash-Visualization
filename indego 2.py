# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:43:17 2019

@author: isaac
"""


from urllib.request import urlopen, Request
import json
import pandas as pd
from pandas.io.json import json_normalize

import time as time2
from datetime import datetime

import os
os.chdir('C:/Users/isaac/Desktop/Data Analytics/Python/Python Projects/Indego Bikeshare')


station_data = [(e['properties']['addressStreet'], e['properties']['addressZipCode'],
                 e['properties']['totalDocks'], e['properties']['kioskId']) for e in data2]

station_data = pd.DataFrame(station_data, columns = ['address', 'zipcode', 'total_docks', 'kioskId'])

live_data = station_data

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

url = 'https://www.rideindego.com/stations/json'


#Return all docks within 19104
data3 = [e['properties']['addressStreet'] for e in data2 if e['properties']['addressZipCode'] == '19104']

a = 0
while True:
    
    webURL = urlopen(Request(url, headers = headers))
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    data_json = json.loads(data.decode(encoding))
    data2 = data_json['features']
    
    new_data = pd.DataFrame([(e['properties']['kioskId'], e['properties']['bikesAvailable']) for e in data2])
    
    time_now = datetime.now().strftime('%Y-%m-%d %H:%M')
    new_data.columns = ['kioskId', time_now]
    live_data = pd.merge(live_data, new_data, on = 'kioskId', how = 'left')

    
    print('Iteration: {}, Time: {}'.format(a, time_now))
    
    a += 1
    #Wait 60s
    for i in range(5):
        time2.sleep(60)
        print('{} min has passed since last request'.format(i + 1))




live_data.to_csv('8 June Bikeshare Data.csv')    
    
    
    
    
    
    
    
    






