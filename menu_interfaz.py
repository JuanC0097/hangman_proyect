import os
from interfaz import dict_ascii

#'''Creacion interfaz inicial del juego
#   Metodos:
#   1. get: obtener del diccionario dict_ascci la lista que alberga las posiciones iniciales del juego
#   2. Guardar en variables las posiciones he imprimirlas'''
def interfaz_inicio():
    inter_compl = dict_ascii.get("intr_inicial")
    saludo = inter_compl[0]
    reglas = inter_compl[1]
    print(saludo,reglas)

#'''Funciones que albergaran las categorias existentes he informacion de estas
#   Metodos:
#   1. get: obtener del diccionario dict_ascci la lista que alberga las posiciones con las categorias
#   2. Guardar en variables las posiciones he imprimirlas'''   
def cate_facil():
    men_facil = dict_ascii.get("menu_facil")
    logo1 = men_facil[0]
    reglas1 = men_facil[1]
    print(logo1,reglas1)

def cate_medio():
    men_medio = dict_ascii.get("menu_Medio")
    logo2 = men_medio[0]
    reglas2 = men_medio[1]
    print(logo2,reglas2)

def cate_dif():
    men_dif = dict_ascii.get("menu_dificil")
    logo3 = men_dif[0]
    reglas3 = men_dif[1]
    print(logo3,reglas3) 
 
#'''Funcion que albergara los estadios del hangman
#   Metodos:
#   1. get: obtener del diccionario dict_ascci la lista que alberga las posiciones de los estados del hangman
#   2. Guardar en variables las posiciones he imprimirlas'''
def state_hang():
    state = dict_ascii.get("state_hangman")
    state1 = state[0]
    state2 = state[1]
    state3 = state[3]
    state4 = state[4]
    state5 = state[5]
    state6 = state[6]
    print(state1,state2,state3,state4,state5,state6)

def categories_ch():
    chosen_categories = dict_ascii.get("categories")
    int_cat = chosen_categories[0]
    int_cat1 = chosen_categories[1]
    print(int_cat,int_cat1)

#Funcion con modulo os importado para limpiar la consola
def clear():
    os.system("clear")   

#Funcion principal la cual guarda el diccionario de listas
def main():
    categories_ch()

#Entry Point
if __name__ == '__main__':
    main()
    