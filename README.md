
![imagen](assets/banco_espana.jpeg)

# Bicimad & Monuments.

:vulcan_salute: Do you like bikes? :bicyclist: 
This application will improve your expirience with Bicimad in Madrid.

## :footprints: First steps.

This is the project for the first module of Inronhack's Bootcamp.

## :thinking: Project:

In this project I am presenting an improvement proposal for the Bicimad and Bicipark applications in Madrid working with the data from both applications and also data containing information about monuments of Madrid.

## :relieved: What does the project do?

The user can choose by terminal the category (Bicimad or Bicipark) and the monument in which he is located.
The application will return:

- The chosen category.

- The monument where you are located.

- The address of the closest place.

- The distance in meters between your location and the category you chose. 

- The availability of the bikes.

> [!NOTE]

I have also implemented the possibility to allow the user to see all the Bicimad and Bicipark stations with their distance, addresses and monuments.

## :star_struck: Why is this project useful?

It is possible to know which is the closest place to find or to leave a bike, the address of that station, the distance to it and the availability of bikes. 

## :robot: Additionally:

- Used libraries:
 
   * Pandas. 
   * Requests.
   * Re.
   * Json.
   * Math.
   * Bs4.
   * Numpy.
   * Argparse.
   * Fuzzywuzzy.

- Data used.

| Place of interest | Place address | BiciMAD station | Station location | Distance | Availability |
|-------------------|---------------|-----------------|------------------|----------|--------------|
| Almacenes Rodríguez | Calle CABALLERO DE GRACIA 3 | Tres Cruces | Calle Tres Cruces nº 7 | 148.15 | 7 |
| ...     | ...            | ...        | ...      | ...        | ...    |

## 	:see_no_evil: Project structure:

``` bash
Proyect_m1/
├── _wip_
├──  assets
│    └── banco_espana.jpeg
│── data
│   ├── bici_monu.csv
│   ├── bicimad_realtime.csv
│   ├── bicimad_stations.csv
│   ├── bicipark_monu.csv
│   ├── bicipark_stations.csv
│   └── colum_bicimad_realtime1.csv
├── modules
│   ├── m_bic_ava.py
│   ├── m_biciMad.py
│   ├── m_biciPark.py
│   ├── m_func_ava.py
│   ├── m_funciones_bicimad.py
│   ├── m_funciones_bicipark.py
│   └── m_json.py
├── notebooks
│   ├── dev_api.ipynb
│   └── dev_notebook_.ipnb
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

 


 



