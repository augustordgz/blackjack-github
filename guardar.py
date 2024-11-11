import json

def guardar_partida():
    usuario = {
        "Nombre": "augusto",
        "Partidas jugadas": "0",
    }
    with open("datos.json", "w") as file:
            datos_usuario = json.dump(usuario, file, indent=4)

guardar_partida()