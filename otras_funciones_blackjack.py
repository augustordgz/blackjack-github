import json
from blackjack import valores

juego = """El objetivo del blackjack es sencillo: cada jugador se enfrenta de forma individual a la banca, en busca de conseguir 21 puntos, o el número más cercano posible., sin pasarse. Para conseguirlos, cada jugador recibe dos cartas al inicio. 

Si las dos primeras cartas suman 21, es la mejor jugada posible, y recibe el nombre de Blackjak. Cuando el jugador no llega a 21, puede pedir cartas extra para llegar, pero si se pasa de los 21 automáticamente pierde.

La banca, que también es parte del juego, tiene sus propias reglas de la casa en blackjack. Recibe dos cartas, y  sus opciones son muy claras:
Si tiene 16 o menos, está obligada a pedir otra carta. 
Si tiene 17 o más se tiene que plantar. 

La banca gana al jugador si este se pasa de 21, y también si este llegara a tener una mano de menor valor que la suya. Si tiene 19 puntos, por ejemplo, le gana a todos los que tengan 18 o menos y 22 o más.
Pierde si el jugador posee una mano superior, o en el caso de que esta exceda los 21 puntos. El empate en blackjack, sucede cuando la banca y el jugador poseen la misma cantidad de puntos.

Una vez repartidas las cartas, empieza el jugador y tiene varias opciones posibles en busca de ganar el juego de blackjack:

Pedir carta: Para llegar a tener Blackjack o acercarse lo más posible, el jugador puede pedir la cantidad de cartas que quiera. Si se pasa de 21, pierde el juego.
Quedarse: Sea al recibir las dos cartas primeras, o luego de pedir más, el jugador de blackjack tiene la opción de quedarse y esperar al final de la ronda.
Turno del crupier: Cuando se termina la ronda del jugador, el crupier gana si el jugador se pasó de 21. Si este no es el caso, el crupier debe ver sus cartas y, si tiene 16 o menos está obligado a pedir otra carta. Si tiene 17 o más está obligado a quedarse.
"""

def valores_cartas():
    return print(valores)

def mostrar_datos():
    try:
        with open("datos.json", "r") as file:
            datos = json.load(file)
            for i in range(len(datos)):
                for j in range(len(datos[i])):
                    print(datos[i][j])
    except FileNotFoundError:
        print("No hay datos guardados para mostrar.")