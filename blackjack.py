import random
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
    global partidas_jugadas, partidas_ganadas, partidas_perdidas, empates, saldo, nombre_usuario
    saldo = 10000
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    jugar = ""
    while jugar != "n":
        print(f"Tu saldo es: {saldo}")
        apuesta = int(input("Ingrese el monto de la apuesta: "))
        while apuesta < 499 or apuesta > saldo:
            print("Ingrese un monto válido (monto mínimo 500)")
            apuesta = int(input("Ingrese el monto de la apuesta: "))
        saldo -= apuesta
        crear_baraja(cartas,palos)
        random.shuffle(baraja)
        mano_jugador = [repartir_carta(baraja),repartir_carta(baraja)]
        mano_crupier = [repartir_carta(baraja),repartir_carta(baraja)]
        print(f"Tu mano es: {mano_jugador} y vale: {valor_mano(mano_jugador)}")
        print(f"Primer carta del crupier: {mano_crupier[0]}.")
        doblar = input("Queres doblar tu apuesta? (s/n): ")
        while doblar.lower() != "s" and doblar.lower() != "n":
            print("Ingrese una opción válida.")
            doblar = input("Queres doblar tu apuesta? (s/n): ")
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

def mostrar_estadisticas():
    print(f"Partidas jugadas: {partidas_jugadas}. Partidas ganadas: {partidas_ganadas}. Partidas perdidas: {partidas_perdidas}. Empates: {empates}.")