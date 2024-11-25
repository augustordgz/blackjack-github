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

cartas = {
    "2_corazones": 2,
    "3_corazones": 3,
    "4_corazones": 4,
    "5_corazones": 5,
    "6_corazones": 6,
    "7_corazones": 7,
    "8_corazones": 8,
    "9_corazones": 9,
    "10_corazones": 10,
    "j_corazones": 10,
    "q_corazones": 10,
    "k_corazones": 10,
    "as_corazones": 11,
    "2_treboles": 2,
    "3_treboles": 3,
    "4_treboles": 4,
    "5_treboles": 5,
    "6_treboles": 6,
    "7_treboles": 7,
    "8_treboles": 8,
    "9_treboles": 9,
    "10_treboles": 10,
    "j_treboles": 10,
    "q_treboles": 10,
    "k_treboles": 10,
    "as_treboles": 11,
    "2_diamantes": 2,
    "3_diamantes": 3,
    "4_diamantes": 4,
    "5_diamantes": 5,
    "6_diamantes": 6,
    "7_diamantes": 7,
    "8_diamantes": 8,
    "9_diamantes": 9,
    "10_diamantes": 10,
    "j_diamantes": 10,
    "q_diamantes": 10,
    "k_diamantes": 10,
    "as_diamantes": 11,
    "2_picas":  2,
    "3_picas":  3,
    "4_picas":  4,
    "5_picas":  5,
    "6_picas":  6,
    "7_picas":  7,
    "8_picas":  8,
    "9_picas":  9,
    "10_picas": 10,
    "j_picas":  10,
    "q_picas":  10,
    "k_picas":  10,
    "as_picas": 11
}