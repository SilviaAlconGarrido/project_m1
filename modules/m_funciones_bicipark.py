import requests #tenemos el json
import pandas as pd
import re #analiza el script para ver si esta bien
import json
import math#operacion matematica
import bs4
import numpy as np
import argparse
import m_json as m
import m_biciPark as bpk

#funcion bicipark
def nearest_bicipark(places, bicipark):
    data_list = []
    
    """ Latitud y longitud a radianes para realizar las operaciones. Luego los convierto a numpy para evitar error. """ 

    places_lat_rad = np.radians(places['latitude_place'].to_numpy())
    places_lon_rad = np.radians(places['longitude_place'].to_numpy())
    bicipark_lat_rad = np.radians(bicipark['latitude_bicipark'].to_numpy())
    bicipark_lon_rad = np.radians(bicipark['longitude_bicipark'].to_numpy())

    dlat = bicipark_lat_rad[:, np.newaxis] - places_lat_rad
    dlon = bicipark_lon_rad[:, np.newaxis] - places_lon_rad

    """ Fórmula de Haversine para calcular las distancias. """ 
    
    a = np.sin(dlat / 2) ** 2 + np.cos(bicipark_lat_rad[:, np.newaxis]) * np.cos(places_lat_rad) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    distance_matrix = c * 6371000 

    """ Cálculo del índice del resultado con menor distancia """

    min_distance_indices = np.argmin(distance_matrix, axis=0)

    """ Creación del dataframe del resultado utilizando ese índice"""

    for x in range(len(places["Place of interest"])):
        station_index = min_distance_indices[x]
        station = bicipark['stationName'].iloc[station_index]
        station_address = bicipark["address"].iloc[station_index]
        place_address = places["address"][x]
        place = places["Place of interest"][x]
        min_distance = round(distance_matrix[station_index, x], 2)
        data_list.append({"place": place, "place_address": place_address, "station_name": station, "station_address": station_address,  "distance": min_distance})
        
    return pd.DataFrame(data_list)

df_f1 = nearest_bicipark(m.df_rename_json, bpk.df_final_bicipark)
print(df_f1)

df_f1.to_csv('./data/bicipark_monu.csv', index=False)