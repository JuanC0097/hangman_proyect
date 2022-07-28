import os
from interfaz import chosen_category
import menu_interfaz
import random
#leer archivo,guardarlo en f
#guardar f en una lista
def read():
    with open ("./word.txt","r", encoding="utf=8") as f:
            list_word = [line for line in f] 
            #reemplezar caracter de la lista
            #agregarlo a nueva lista
            words = []   
            for line in list_word:
                result = line.replace('\n','')
                words.append(result)
    
    print(random.choice(words))

#funcion para escoguer la categoria.
def categoria(dificultad,categoria):
    eleccion = int(input("Por favor Ingrese la categoria a la cual desea ingresar"))

    if (categoria) == (dificultad):
        print
    
def run():
    #limpia consola
    menu_interfaz.clear()
    #art-ascii "inicio"
    menu_interfaz.interfaz_inicio()
    #categorias con las que contamos
    menu_interfaz.categories_ch()
    print(read())

if __name__ == '__main__':
    run()
