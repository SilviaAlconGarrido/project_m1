import requests #tenemos el json
import pandas as pd
import re #analiza el script para ver si esta bien
import json
import math#operacion matematica
import bs4
import numpy as np
import argparse


json_monumentos = 'https://datos.madrid.es/egob/catalogo/208844-0-monumentos-edificios.json'
    #print(type(json_monumentos))

response  = requests.get(json_monumentos)

    #parsea el contenido como un json
json = response.json()
json['@graph']

df_json = pd.json_normalize(json['@graph'])
    #df_json

df_column_json = df_json[['title', 'address.street-address', 'location.latitude', 'location.longitude']]
    #print(df_column_json)

df_rename_json = df_column_json.rename(columns={'title':'Place of interest',
                                                'address.street-address':'address',
                                                'location.latitude':'latitude_place',
                                                'location.longitude':'longitude_place'})
#print(df_rename_json)


