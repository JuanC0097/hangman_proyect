import os

def clear():
    os.system("clear")

dict_ascii= { 
    "intr_inicial": ['''
            ##########################################################################################   
            # __                                                                                     #
            #| |                                                                                     #
            #| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __               __ _  __ _ _ __ ___  _ _ _  #
            #| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \   _______   / _` |/ _` | '_ ` _ \|  _ _) #
            #| | | | (_| | | | | (_| | | | | | | (_| | | | |  |_/_/_/|   (_| | (_| | | | | | | ( )   #
            #|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|            \__, |\__,_|_| |_| |_|_____) #
            #                    __/ |                                   __/ |                       #
            #                   |___/                                   |___ |                       #
            ##########################################################################################
                    ''','''

             ########################################################################################
             #                               Reglas del Juego                                       #
             #                                                                                      #
             #               1.No Puedes ingresar numeros                                           #
             #                                                                                      #
             #               2.Solo puedes ingresar un caracter                                     #
             #                                                                                      #
             #               3.Por favor ingresar los caracteres en mayuscula                       #
             #                                                                                      #
             #          4.El juego terminara cuando encuentres la palabra o agotes tus intentos     #
             #                                                                                      #
             ########################################################################################
            
            ''']
    
            }



def run():
    clear()
    print()

    print("Las Categorias son:"+"\n1.FACIL\n2.NORMAL\n3.DIFICIL")
    categoria = int(input("Por favor elija la categoria: "))
    if categoria == 1:
        print("Ha seleccionado la categoria FACIL")
        categoria == int(categoria)
        print(categoria)
    elif categoria == 2:
        print("Ha seleccionado la categoria NORMAL")
        categoria == int(categoria)
        print(categoria)
    elif categoria == 3:
        print("Ha seleccionado la categoria DIFICIL")
        categoria == int(categoria)
        print(categoria)
    else:
        print("No ha seleccionado una categoria")



if __name__ == '__main__':
    run()
    
