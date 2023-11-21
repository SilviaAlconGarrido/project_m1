

# Bicimad y Edificios de carácter monumental.

:vulcan_salute: ¿Te gustan las bicis? :bicyclist: 
Esta aplicación te ayudara a mejor tu experiencia con Bicimad en Madrid.

## :footprints: Primeros pasos.

Esto es el primer proyecto del modulo 1 del bootcamp de Ironhack.

## :thinking: Project:

En este proyecto presentamos una propuesta de mejora para la aplicación de Bicimad y Bicipark de la Comunidad de Madrid. En el trabajamos con los datos tanto de Bicimad, Bicipark y los monumentos de carácter monumental de la Comunidad de Madrid.

## :relieved: ¿Qué hace el proyecto?

El usuario pide por terminal la categoría que quiere si bicimad o bicipark y el monumento de carácter monumental en el que se encuentra. 
La aplición te devuelve :

- La categoría que elegiste.

- El monumento en el que te encuentras.

- La dirección del lugar más cercano.

- La distancia en metros de la que te encuentras de la categoría que elegiste. 

- La disponibilidad de las bicis que hay.

> [!NOTE]

También hemos implementado que el usario pueda ver todas las estaciones de bicimad o bicipark con sus distancias, direcciones y demas monumentos.

## :star_struck: ¿Por qué el proyecto es útil?

Puedes saber el lugar mas cercano donde poder encontrar una bici o poder dejarla. Saber en que calle se encuentra y la distancia en la que se encuentra. Y la disponibilidad en ese preciso instante. 

## :robot: Additionally:

- Librerias con las que trabajadas:
 
   * Pandas. 
   * Requests.
   * Re.
   * Json.
   * Math.
   * Bs4.
   * Numpy.
   * Arparse.
   * Fuzzywuzzy.

- Datos con los que trabajados.

| Place of interest | Place address | BiciMAD station | Station location | Distance | Availability |
|-------------------|---------------|-----------------|------------------|----------|--------------|
| Almacenes Rodríguez | Calle CABALLERO DE GRACIA 3 | Tres Cruces | Calle Tres Cruces nº 7 | 148.15 | 7 |
| ...     | ...            | ...        | ...      | ...        | ...    |

## 	:see_no_evil: Estructura del proyecto:
Proyect 
├── _wip_
|── assets
│    └── banco_espana.jpeg
│── data
│   ├── bici_monu.csv
│   ├── bicimad_realtime.csv
│   ├── bicimad_stations.csv
│   ├── bicipark_monu.csv
│   ├── bicipark_stations.csv
│   └── colum_bicimad_realtime1.csv
├── modules
|   ├── m_bic_ava.py
│   ├── m_biciMad.py
│   ├── m_biciPark.py
│   ├── m_func_ava.py
│   ├── m_funciones_bicimad.py
│   ├── m_funciones_bicipark.py
│   └── m_json.py
├── notebooks
|   ├── dev_api.ipynb
│   └── dev_notebook_.ipnb
├── .gitignore
├── LICENSE
├── main.py
└── README.md


 


 



[image]: assets/banco_espana.jpeg