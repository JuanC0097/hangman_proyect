import os
import menu_interfaz
import random
#'''leer archivo,guardarlo en una lista|funcion: with(Abrir y Cerrar archivos)
#Metodos: replace(eliminar salto de linea) append(nueva lista sin salto de linea)
# '''
def read():
    with open ("./word.txt","r", encoding="utf=8") as f:
            list_word = [line for line in f]
            words = []

            for i in list_word:
                result = i.replace('\n','')              
                words.append(result)
    return(words)

#Limpiar acentos| metodos: maketrans y translate.
def clearvocal():
    words = str(read())
    new_words = words.maketrans('áéíóú', 'aeiou')
    nwords = words.translate(new_words)
    return(nwords)

#'''Funcion principal
#   1. Limpiar consola: funcion importada del archivo menu_interfaz
#   2. Arte ascci: nombre del programa y categorias existentes
#   3. estructura de control if/else: escoguer la categoria'''
def run():
    menu_interfaz.clear()
    menu_interfaz.interfaz_inicio()
    menu_interfaz.categories_ch()
    
    chosen = int(input("Por favor Ingrese la categoria a la cual desea ingresar: "))
    if chosen == 1:
        menu_interfaz.cate_facil()
    else:
        if chosen == 2:
            menu_interfaz.cate_medio()
        else:
            if chosen == 3:
                menu_interfaz.cate_medio()
            else:
                print("Por favor Ingrese una categoria valida") 
    
    print(clearvocal())

if __name__ == '__main__':
    run()
