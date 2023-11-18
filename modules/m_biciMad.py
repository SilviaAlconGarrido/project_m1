import requests #tenemos el json
import pandas as pd
import re #analiza el script para ver si esta bien
import json
import math#operacion matematica
import bs4
import numpy as np
import argparse


df_bicimad_stations = pd.read_csv('./data/bicimad_stations.csv', sep= '\t')
    #print(df_bicimad_stations)

column = df_bicimad_stations[['name', 'address','activate', 'geometry.coordinates']]
#print(column)

    # Ahora hay que separar las coordenadas por longitud y latitud
    #primero sacamos los [] y separamos por ',' 
split_bicimad = column['geometry.coordinates'].str.strip('[]').str.split(',', expand=True).astype('float64')

    #ahora lo metemos en dos nuevas columnas que las llamamos longitus y latitud
split_bicimad.columns = ['longitude_bicimad', 'latitude_bicimad']

    #unimos estas dos columnas al anterior df
df_column_bicimad = pd.concat([column, split_bicimad], axis=1)
    #print(df_column_bicimad)
        
df_final_bicimad = df_column_bicimad[['name', 'address','activate', 'longitude_bicimad', 'latitude_bicimad']]
#print(df_final_bicimad)



