import json

def guardar_partida(nombre, partidas_jugadas, partidas_ganadas, partidas_perdidas, empates):
    try:
        with open("datos.json", "r") as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = []
    usuario = {
        "Nombre": nombre,
        "Partidas Jugadas": partidas_jugadas,
        "Partidas Ganadas": partidas_ganadas,
        "Partidas Perdidas": partidas_perdidas,
        "Partidas Empatadas": empates
    }
    datos.append(usuario)
    with open("datos.json", "w") as file:
        json.dump(datos, file, indent=4)

