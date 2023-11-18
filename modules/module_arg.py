import argparse
import df_bicimad_stations from modules.m_biciPArk

def bicimad(c: str, dest: str):
    c = input('Elige entre Bicimad o Bicipark: ')
    print(f'Elegiste: {c}')
    print(f'En el lugar: {dest}')
    

def bicipark(c: str, dest: str):
    c = input('Elige entre Bicimad o Bicipark: ')
    print(f'Elegiste: {c}')
    print(f'En el lugar: {dest}')
   
    

# Argument parser function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Esta es una aplicación para encontrar una estación de bicimad o bicipark dependiendo del Edificios de carácter monumental en el que estes.' )
    help_message ='Debes introducir un Edificios de carácter monumental de Madrid'
    help_category ='Elige entre Bicimad o Bicipark'
    help_all ='Aqui te devuelve todo'
    parser.add_argument('-c', '--category', help=help_category, type=str)
    parser.add_argument('-a', '--a', help=help_all, type=str)
    parser.add_argument('-h','--help', help=help_message, type=str )
    args = parser.parse_args()
    
# Pipeline execution

    if args.cat == 'Bicimad':
        dest = input('Introduce un Edificio de carácter monumental: ')
        bicimad(args.c) 
    elif args.cat == 'Bicipark':
        c = input('Elige entre Bicimad o Bicipark: ')
        dest = input('Introduce un Edificio de carácter monumental: ')
        bicipark(args.c)
    elif args.a == 'all':
        print('Este Edificios de carácter monumental no esta. Prueba con otro.')
    
    
