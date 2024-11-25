import random
import pygame
from guardar import *

cartas = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
palos = ["Diamantes","Trérboles","Picas","Corazones"]
valores = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}
baraja = []
partidas_jugadas = 0
partidas_ganadas = 0
partidas_perdidas = 0
empates = 0
saldo = 0
nombre_usuario = ""

def crear_baraja(cartas, palos):
    for carta in cartas:
        for palo in palos:
            baraja.append([carta, palo])
    return baraja

def repartir_carta(baraja):
    return baraja.pop(random.randint(0,len(baraja) - 1))

def valor_mano(mano):
    total = 0
    aces = 0
    for carta, _ in mano:
        total += valores[carta]
        if carta == "A":
            aces += 1
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def jugar():
    """
    Esta es la funcion principal para jugar al BlackJack.
    Variables globales utilizadas:
    - partidas_jugadas: Número total de partidas jugadas.
    - partidas_ganadas: Número de partidas ganadas por el jugador.
    - partidas_perdidas: Número de partidas perdidas por el jugador.
    - empates: Número de partidas empatadas.
    - saldo: Dinero disponible para el jugador.
    - nombre_usuario: Nombre ingresado por el jugador.

    Lógica:
    1. El jugador ingresa su nombre y juega varias rondas hasta decidir salir o quedarse sin saldo.
    2. En cada ronda, el jugador apuesta y juega en su turno (puede pedir cartas o quedarse).
    3. Al final de la ronda, se determina si el jugador gana, pierde o empata.
    
    """
    global partidas_jugadas, partidas_ganadas, partidas_perdidas, empates, saldo, nombre_usuario
    saldo = 10000 #saldo inicial del jugador
    nombre_usuario = input("Ingrese su nombre de usuario: ") #solicita un nombre al usuario
    jugar = "" # variable de control para continuar o salir del juego
    
    # bucle principal del juego donde el jugador elige si seguir jugando o no
    while jugar != "n":
        print(f"Tu saldo es: {saldo}")#te muestra tu saldo actual
        apuesta = int(input("Ingrese el monto de la apuesta: "))# solicita el monto que se quiere apostar 
        # valida que la apuesta sea un valor permitido para apostar minimamente
        while apuesta < 500 or apuesta > saldo:
            print("Ingrese un monto válido (monto mínimo 500)")
            apuesta = int(input("Ingrese el monto de la apuesta: "))
        # resta el monto de la apuesta al saldo del jugador 
        saldo -= apuesta 
        # inicializa y mezcla la baraja de cartas
        crear_baraja(cartas,palos)
        random.shuffle(baraja)
        # reparte dos cartas iniciales para el jugador y el crupier
        mano_jugador = [repartir_carta(baraja),repartir_carta(baraja)]
        mano_crupier = [repartir_carta(baraja),repartir_carta(baraja)]
        # muestra la mano inicial del jugador y l aprimer carta del crupier
        print(f"Tu mano es: {mano_jugador} y vale: {valor_mano(mano_jugador)}")
        print(f"Primer carta del crupier: {mano_crupier[0]}.")
        # ofrece al jugador la opcion de doblar el valor de su apuesta
        doblar = input("Queres doblar tu apuesta? (s/n): ")
        while doblar.lower() != "s" and doblar.lower() != "n":
            print("Ingrese una opción válida.")
            doblar = input("Queres doblar tu apuesta? (s/n): ")
        # en caso de no doblar la apuesta, permite pedir cartas (SEGUI DOCUMENTANDO A PARTIR DE ACA)
        while valor_mano(mano_jugador) < 21 and doblar == "n":
            indicacion = input("¿Queres pedir otra carta (p) o quedarte (q)? (p/q): ")
            while indicacion.lower() != "q" and indicacion.lower() != "p":
                print("Ingrese una indicación válida (p/q)")
                indicacion = input("¿Queres pedir otra carta (p) o quedarte (q)? (p/q): ")
            if indicacion.lower() == "p":
                mano_jugador.append(repartir_carta(baraja))
                print(f"Tu mano es: {mano_jugador} y vale: {valor_mano(mano_jugador)}.")
                if valor_mano(mano_jugador) > 21:
                    break
            elif indicacion.lower() == "q":
                break
        if doblar == "s":
            saldo -= apuesta
            apuesta = apuesta*2
            print(f" ------- Tu nueva apuesta es: {apuesta} ------- ")
            mano_jugador.append(repartir_carta(baraja))
            print(f"Tu mano es: {mano_jugador} y vale: {valor_mano(mano_jugador)}.")
        if valor_mano(mano_jugador) > 21:
                print("Perdiste, Te pasaste de 21.")
                partidas_perdidas += 1
                apuesta = 0
                print(f" ------- Tu nuevo saldo es: {saldo} ------- ")
        else:
            print(f"La mano del crupier es: {mano_crupier} y vale: {valor_mano(mano_crupier)}")
            while valor_mano(mano_crupier) < 17:
                if valor_mano(mano_crupier) > valor_mano(mano_jugador):
                    break
                mano_crupier.append(repartir_carta(baraja))
                print(f"El crupier pide otra carta. La mano del crupier es: {mano_crupier} y vale: {valor_mano(mano_crupier)}")
            if valor_mano(mano_crupier) > 21:
                print("El crupier se pasó de 21. ¡Ganaste!")
                partidas_ganadas += 1
                saldo += apuesta*2
                apuesta = 0
                print(f" ------- Tu nuevo saldo es: {saldo} ------- ")
            elif valor_mano(mano_jugador) > valor_mano(mano_crupier):
                print("Tu mano vale más que la del crupier, ¡Ganaste!")
                partidas_ganadas += 1
                saldo += apuesta*2
                apuesta = 0
                print(f"Tu nuevo saldo es: {saldo}")
            elif valor_mano(mano_jugador) < valor_mano(mano_crupier):
                print("La mano del crupier vale más que la tuya, perdiste.")
                partidas_perdidas += 1
                apuesta = 0
                print(f" ------- Tu nuevo saldo es: {saldo} ------- ")
            else:
                print("Empate.")
                empates += 1
                saldo += apuesta
                apuesta = 0
                print(f" ------- Tu nuevo saldo es: {saldo} ------- ")
        if saldo < 499:
            print("Te quedaste sin saldo. Reinicia el juego para poder volver a jugar.")
            break
        partidas_jugadas += 1
        jugar = input("¿Quieres seguir jugando? (s/n): ")
        if jugar == "n":
            guardar_partida()
