from blackjack import jugar, mostrar_estadisticas
from otras_funciones_blackjack import *

def menu():
    salir = ""
    while salir != "salir":
        print("\nMenu:")
        print("1. Jugar partida.")
        print("2. Como jugar.")
        print("3. Mostrar valores de las cartas.")
        print("4. Mostrar estadísticas.")
        print("5. Mostrar rankings.")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            jugar()
        elif opcion == '2':
            print(juego)
        elif opcion == '3':
            valores_cartas()
        elif opcion == '4':
            mostrar_estadisticas()
        elif opcion == '5':
            pass
        elif opcion == '6':
            print("Saliendo..")
            salir = "salir"
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

menu()