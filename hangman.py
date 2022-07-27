import os
from interfaz import chosen_category
import menu_interfaz

#leer archivo,guardarlo en f
#guardar f en una lista
def read():
    with open ("./word.txt","r", encoding="utf=8") as f:
            list_word = [line for line in f]       
    return list_word

def word(letter):
    letter = letter.replace('\n', '')
    letter = letter

def categorie():
    menu_interfaz.clear()
    menu_interfaz.interfaz_inicio()
    menu_interfaz.categories_ch()
    chosen = int(input("Por favor ingresa el numero de la categoria, que deseas jugar: "))
    if chosen == 1:
        menu_interfaz.cate_facil()
    elif chosen == 2:
        menu_interfaz.cate_medio()
    elif chosen == 3:
        menu_interfaz.cate_dif()
    else:
        print("Por favor ingresa una categoria valida (1  2  3)")
    return chosen

def run():
    read()
    
    #correct = word(letter)
    #if correct == True:
    #        print("La letra esta en la palabra")
    #else:
    #    print("La letra no se encuentra")

if __name__ == '__main__':
    run()
