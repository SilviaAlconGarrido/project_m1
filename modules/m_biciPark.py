import requests #tenemos el json
import pandas as pd
import re #analiza el script para ver si esta bien
import json
import math#operacion matematica
import bs4
import numpy as np
import argparse


df_bicipark_stations = pd.read_csv('./data/bicipark_stations.csv', sep= ';')
    #print(df_bicipark_stations)

column_bicipark = df_bicipark_stations[['stationName', 'address', 'geometry.coordinates']]
    #print(column_bicipark)

    # Ahora hay que separar las coordenadas por longitud y latitud
    #primero sacamos los [] y separamos por ',' 
split_bicipark = column_bicipark['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype('float64')

    #ahora lo metemos en dos nuevas columnas que las llamamos longitus y latitud
split_bicipark.columns = ['longitude_bicipark', 'latitude_bicipark']

    #unimos estas dos columnas al anterior df
df_column_bicipark = pd.concat([column_bicipark, split_bicipark], axis=1)
    #print(df_column_bicipark)

    #nos quedamos con las columnas sin geometry.coordinates
df_final_bicipark = df_column_bicipark[['stationName', 'address', 'longitude_bicipark', 'latitude_bicipark']]
    #print(df_final_bicipark)

