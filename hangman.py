import os
import menu_interfaz
import random
#leer archivo,guardarlo en f
#guardar f en una lista
def read():
    with open ("./word.txt","r", encoding="utf=8") as f:
            list_word = [line for line in f] 
            #reemplazar caracter de la lista
            #agregarlo a nueva lista
            words = []
            for i in list_word:
                result = i.replace('\n','')              
                words.append(result)
    return(words)
    #print(random.choice(words))   

vocales = {
    'á':'a',
    'é':'e',
    'í':'i',
    'ó':'o',
    'ú':'u',    
}

def change_voca():
    list_word = str(read())
    list_word.join(vocales.get(c, c) for c in list_word)
    return list_word

def run():
    #limpia consola
    menu_interfaz.clear()
    #art-ascii "inicio"
    menu_interfaz.interfaz_inicio()
    #categorias con las que contamos
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
                print("Por favor Ingrese una categorita valida") 
    
    change_voca()  

if __name__ == '__main__':
    run()
