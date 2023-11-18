
import argparse
import pandas as pd
#Esto me devuelve lod df enteros
def resumen(categoria):
    df_biciMadf =  pd.read_csv('./data/bici_monu.csv')
    df_biciParkf = pd.read_csv('./data/bicipark_monu.csv')
    if categoria == 'Bicimad':
        print(f'Elegiste: {categoria}')
        print(df_biciMadf)
    elif categoria == 'Bicipark':
        print(f'Elegiste: {categoria}')
        print(df_biciMadf)


#Esto me hace elegir entre Bicimad y bicipark pediendome el sitio
def elegir(categoria, sitio):
    df_biciMadf =  pd.read_csv('./data/bici_monu.csv')
    df_biciParkf = pd.read_csv('./data/bicipark_monu.csv')

    print(f'Elegiste: {categoria}')
    print(f'En el lugar: {sitio}')
    if categoria == 'Bicimad':
        print(f'El bicimad más cercano es: {df_biciMadf[df_biciMadf["place"]==sitio]["station_address"].iloc[0]} ')
        print(f'En esta distancia: {df_biciMadf[df_biciMadf["place"]==sitio]["distance"].iloc[0]} metros')
        #print(df_biciMadf[df_biciMadf['place']==sitio][["place_address", "station_name","station_address", "distance"]])
        #return df_biciMadf[df_biciMadf['place']==sitio]

    if categoria == 'Bicipark':
        print(f'El Bicipark más cercano es: {df_biciParkf[df_biciParkf["place"]==sitio]["station_name"].iloc[0]}')
        print(f'En esta distancia: {df_biciParkf[df_biciParkf["place"]==sitio]["distance"].iloc[0]} metros')
        #print(df_biciParkf[df_biciParkf['place']==sitio][["place_address", "station_name","station_address", "distance"]])

    else:
        return('Elige entre Bicimad y Bicipark')
   
# Argument parser function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Esta es una aplicación para encontrar una estación de bicimad o bicipark dependiendo del Edificios de carácter monumental en el que estes.' )
    help_category ='Elige entre Bicimad o Bicipark'
    help_all ='Aqui te devuelve todo'
    parser.add_argument('-r', help="-r y Elige Bicimad o Bicipark", type=str)
    parser.add_argument('-c', help=help_category, type=str)
    parser.add_argument('-s', help=help_all, type=str)
    args = parser.parse_args() 
    resumen(args.r)
    elegir(args.c, args.s)  