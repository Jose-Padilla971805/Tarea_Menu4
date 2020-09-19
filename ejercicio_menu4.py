import os
from taller1 import ejercicio1 
from taller2 import ejercicio2 
from taller3 import ejercicio3 
from taller4 import ejercicio4 



def menu():

    os.system("pause")
    os.system("cls")

    while(True):

        print("           Bienvenido      ")
        print("                           ")
        print("  1. ejercicio 1           ")
        print("  2. ejercicio 2           ")
        print("  3. ejercicio 3           ")
        print("  4. ejercicio 4           ")
        print("  5. salir                 ")
        print("                           ")
        print("   por favor elige una opción   ")


        print("")

        item = int(input("indicanos que deseas revisar? => "))
        print("")
        if item == 1:
            print("Has seleccionado el taller 1 , estas atento? \n")
            ejercicio1()
        elif item == 2:
            print("Has seleccionado el taller 2, estas atento? \n")
            ejercicio2()
        elif item == 3:
            print("Has seleccionado el taller 3, estas atento? \n")
            ejercicio3()
        elif item == 4:
            print("Has seleccionado el taller 4, estas atento? \n")
            os.system("pause")
            os.system("cls")
            ejercicio4()
        elif item ==5:
            print("Gracias... \n")
            break
        else:
            print("... Opción no valida, intente nuevamente \n")
            break
        os.system("pause")
        os.system("cls")


def main():
    menu()

if __name__ == "__main__":
    main()