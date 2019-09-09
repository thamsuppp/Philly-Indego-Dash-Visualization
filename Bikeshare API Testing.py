# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 00:07:31 2019

@author: isaac
"""

import json
import requests
import pandas as pd


api_url = 'https://dkw6qugbfeznv.cloudfront.net/'
response = requests.get(api_url)

data = json.loads(response.content.decode('utf-8'))

data = data['features']

stations = [{'x_coord': e['geometry']['coordinates'][0],
             'y_coord': e['geometry']['coordinates'][1],
            'address': e['properties']['addressStreet'],
            'kioskId': e['properties']['kioskId']} for e in data]

stations_df = pd.DataFrame(stations)


stations_df.x_coord.mean()