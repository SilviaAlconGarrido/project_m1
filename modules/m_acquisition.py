import requests #tenemos el json
import pandas as pd
import re #analiza el script para ver si esta bien
import json
import math#operacion matematica
import bs4
import numpy as np
import argparse

def acquire():
    json_monumentos = 'https://datos.madrid.es/egob/catalogo/208844-0-monumentos-edificios.json'
    print(type(json_monumentos))
    df_bicimad_stations = pd.read_csv('../data/bicimad_stations.csv', sep= '\t')
    df_bicimad_stations
    df_bicipark_stations = pd.read_csv('../data/bicipark_stations.csv', sep= ';')
    df_bicipark_stations