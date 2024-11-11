import json

def guardar_partida():
    from blackjack import nombre_usuario, partidas_jugadas, partidas_ganadas, partidas_perdidas, empates, saldo
    usuario = {
        "Nombre": {nombre_usuario},
        "Partidas Jugadas": {partidas_jugadas},
        "Partidas Ganadas": {partidas_ganadas},
        "Partidas Perdidas": {partidas_perdidas},
        "Partidas Empatadas": {empates},
        "Saldo": {saldo}
        }
    with open("datos.json", "w") as file:
            json.dump(usuario, file, indent=4)
