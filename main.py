import argparse


# Script functions 

def bicimad(c: str, dest: str):
    c = input('Elige entre Bicimad o Bicipark: ')
    dest = input('Introduce un Edificio de carácter monumental: ')
    print(f'Elegiste: {c}')
    print(f'En el lugar: {dest}')

def bicipark(c: str, dest: str):
    c = input('Elige entre Bicimad o Bicipark: ')
    dest = input('Introduce un Edificio de carácter monumental: ')
    print(f'Elegiste: {c}')
    print(f'En el lugar: {dest}')
    

# Argument parser function
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Esta es una aplicación para encontrar una estación de bicimad o bicipark dependiendo del Edificios de carácter monumental en el que estes.' )
    help_message ='Debes introducir un Edificios de carácter monumental de Madrid'
    help_category ='Elige entre Bicimad o Bicipark'
    parser.add_argument('-c', '--category', help=help_message, type=str)
    args = parser.parse_args()
    #return args.e


# Pipeline execution

#if __name__ == '__main__':
    parser = argparse.ArgumentParser(description= 'Esta es una aplicación para encontrar una estación de bicimad o bicipark dependiendo del Edificios de carácter monumental en el que estes.' )
    help_message ='Debes introducir un Edificios de carácter monumental de Madrid' 
    parser.add_argument('-e', '--edificio', help=help_message, type=str)
    args = parser.parse_args()
    #return args.e
    
    if args.e == 'bicimad':
        bicimad(args.e)
    elif args.e == 'bicipark':
        bicipark(args.e)
    else:
        print('Este Edificios de carácter monumental no esta. Prueba con otro.')
    
    
