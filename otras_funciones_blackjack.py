import json

def mostrar_datos():
    datos_a_mostrar = []
    try:
        with open("datos.json", "r") as file:
            datos = json.load(file)
            for i in range(len(datos)):
                for j in range(len(datos[i])):
                    datos_a_mostrar.append(datos[i][j])
    except FileNotFoundError:
        datos_a_mostrar.append("No hay datos guardados para mostrar.")
    return datos_a_mostrar