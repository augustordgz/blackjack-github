from constantes import BLANCO
import json

def guardar_partida(nombre, partidas_jugadas, partidas_ganadas, partidas_perdidas, empates):
    """
    |Guarda los datos de una partida en un archivo JSON.
    |Argumentos:
        nombre (str): El nombre del jugador.
        partidas_jugadas (int): Numero total de partidas jugadas por el jugador.
        partidas_ganadas (int): Numero de partidas ganadas por el jugador.
        partidas_perdidas (int): Numero de partidas perdidas por el jugador.
        empates (int): Numero de partidas empatadas por el jugador.
    |Retorna:
        None ,La funcion no devuelve ningun valor. Los datos se guardan directamente en el archivo "datos.json".
    """
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

def mostrar_datos_pygame(ventana):
    """
    |Muestra los datos de los usuarios almacenados en un archivo JSON en una ventana usando Pygame.
    |Argumentos:
        ventana (pygame.Surface): La superficie de Pygame donde se renderizaran los datos.
    |Retorna:
        None ,la funcion no devuelve ningun valor. Los datos se muestran directamente en la ventana.
    """
    from main import font
    try:
        with open("datos.json", "r") as file:
            datos = json.load(file)
            y_offset = 40  # Posicion vertical para imprimir cada linea
            for usuario in datos:
                # Cada dato se convierte en una linea y se renderiza
                nombre = font.render(f"Nombre: {usuario['Nombre']}", True, BLANCO)
                partidas_jugadas = font.render(f"Partidas Jugadas: {usuario['Partidas Jugadas']}", True, BLANCO)
                partidas_ganadas = font.render(f"Partidas Ganadas: {usuario['Partidas Ganadas']}", True, BLANCO)
                partidas_perdidas = font.render(f"Partidas Perdidas: {usuario['Partidas Perdidas']}", True, BLANCO)
                partidas_empates = font.render(f"Partidas Empatadas: {usuario['Partidas Empatadas']}", True, BLANCO)
                # Mostrar los textos en la pantalla
                ventana.blit(nombre, (30, y_offset))
                y_offset += 40
                ventana.blit(partidas_jugadas, (30, y_offset))
                y_offset += 40
                ventana.blit(partidas_ganadas, (30, y_offset))
                y_offset += 40
                ventana.blit(partidas_perdidas, (30, y_offset))
                y_offset += 40
                ventana.blit(partidas_empates, (30, y_offset))
                y_offset += 50  # Espacio entre los jugadores
    except FileNotFoundError:
        mensaje = font.render("No hay datos guardados para mostrar.", True, BLANCO)
        ventana.blit(mensaje, (30, 40))