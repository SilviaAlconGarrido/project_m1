import requests #tenemos el json
import pandas as pd
import re #analiza el script para ver si esta bien
import json
import math#operacion matematica
import bs4
import numpy as np
import argparse
import m_json as m
import m_biciMad as bm
#funcion bicimad:

def nearest_bicimad(places, bicimad):
    data_list = []
    
    """ Latitud y longitud a radianes para realizar las operaciones. Luego los convierto a numpy para evitar error. """ 

    places_lat_rad = np.radians(places['latitude_place'].to_numpy())
    places_lon_rad = np.radians(places['longitude_place'].to_numpy())
    bicimad_lat_rad = np.radians(bicimad['latitude_bicimad'].to_numpy())
    bicimad_lon_rad = np.radians(bicimad['longitude_bicimad'].to_numpy())

    dlat = bicimad_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicimad_lon_rad[:, np.newaxis] - places_lon_rad

    """ Fórmula de Haversine para calcular las distancias. """ 
    
    a = np.sin(dlat / 2) ** 2 + np.cos(bicimad_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    """ Cálculo del índice del resultado con menor distancia """

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    """ Creación del dataframe del resultado utilizando ese índice"""

    for x in range(len(places["Place of interest"])):
        station_index = min_distance_indices[x]
        station = bicimad['name'].iloc[station_index].split('- ')[1]
        station_address = bicimad["address"].iloc[station_index]
        place_address = places["address"][x]
        place = places["Place of interest"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        activate_index = bicimad['activate'].iloc[station_index]
        data_list.append({"place": place, "place_address": place_address, "station_name": station, "station_address": station_address,  "distance": min_distance})
        
    return pd.DataFrame(data_list)

df_f = nearest_bicimad(m.df_rename_json, bm.df_final_bicimad)
#print(df_f)   

#aqui creamos el csv de bicimad

df_f.to_csv('./data/bici_monu.csv', index=False)
