import requests
import os
import json
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import re

def get_token():
    load_dotenv('./.env')
    email = "silvi.alcon5@gmail.com"
    password = os.environ.get("password")
    url = "https://openapi.emtmadrid.es/v3/mobilitylabs/user/login/"
    headers = {"email": email, "password" : password}
    response = requests.get(url, headers=headers)
    return response.content

def get_available_bikes():
    load_dotenv("./.env")
    token = os.environ.get("access_token")
    url = "https://openapi.emtmadrid.es/v3/transport/bicimad/stations/"
    headers = {"accessToken" : token}
    response = requests.get(url, headers = headers).json()
    return response

stations_real_time = get_available_bikes()
bicimad_real_time = pd.DataFrame(stations_real_time["data"])
print(bicimad_real_time)
'''
colum_bicimad_real_time = bicimad_real_time[['address','dock_bikes', 'geometry']]
print(colum_bicimad_real_time)

geometry_bicimad = colum_bicimad_real_time['geometry']
#type(geometry_bicimad)
#print(geometry_bicimad)

colum_bicimad_real_time['geometry'].apply(lambda x: pd.Series(x['coordinates']))

long_lat = colum_bicimad_real_time[['longitude', 'latitude']]

df_final_realtime = colum_bicimad_real_time[[ 'address','dock_bikes', 'longitude', 'latitude']]
#df_final_realtime

print(df_final_realtime.to_csv('./data/bicimad_realtime.csv', index=False))
'''