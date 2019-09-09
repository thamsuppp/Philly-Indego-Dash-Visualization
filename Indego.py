# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:13:52 2019

@author: isaac
"""
import os
import pandas as pd
from datetime import datetime, date, time
import matplotlib.pyplot as plt

#https://realpython.com/python-matplotlib-guide/

os.chdir('C:/Users/isaac/Desktop/Data Analytics/Python/Python Projects/Indego Bikeshare')

indego = pd.read_csv('indego-trips-2019-q1.csv')

#Average duration of trip - 20.87 min
indego['duration'].mean()

#Change start time to a datetime 
indego['start_time'] = indego['start_time'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

indego['start_hour'] = indego['start_time'].apply(lambda x: x.hour)

#Distribution of Indego Trips by Hour of Start Time

start_hour = indego.groupby('start_hour')['start_hour'].count()
start_hour.plot.bar()

#Distribution of Indego Trip Durations by Hour of Start Time

duration_by_hour = indego.groupby('start_hour')['duration'].mean()
duration_by_hour.plot.bar()

stations = pd.read_csv('indego-stations-2019-04-01.csv')

stations_names = stations.iloc[:, 0:2]

#Join station_names to indego dataframe

indego = indego.merge(stations_names, left_on = 'start_station',
                                    right_on = 'Station ID', how = 'left')

indego = indego.merge(stations_names, left_on = 'end_station',
                                    right_on = 'Station ID', how = 'left')

indego = indego.loc[:, ['trip_id', 'duration', 'start_time', 'end_time', 'start_station', 'Station Name_x',
                        'start_lat', 'start_lon', 'end_station', 'Station Name_y', 'end_lat', 'end_lon',
                        'bike_id', 'plan_duration', 'trip_route_category', 'passholder_type','bike_type']]
