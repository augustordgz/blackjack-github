import json

def guardar_partida():
    from blackjack import nombre_usuario, partidas_jugadas, partidas_ganadas, partidas_perdidas, empates, saldo
    try:
        with open("datos.json", "r") as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = []
    usuario = [f"Nombre: {nombre_usuario}", f"Partidas Jugadas: {partidas_jugadas}", f"Partidas Ganadas: {partidas_ganadas}", f"Partidas Perdidas: {partidas_perdidas}", f"Partidas Empatadas: {empates}", f"Saldo: {saldo}"]
    datos.append(usuario)
    with open("datos.json", "w") as file:
            json.dump(datos, file, indent=4)
