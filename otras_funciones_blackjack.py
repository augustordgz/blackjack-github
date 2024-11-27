from constantes import BLANCO
import json
import pygame

def mostrar_datos_pygame(ventana):
    font = pygame.font.Font("assets/fonts/static/PixelifySans-Medium.ttf", 36)  # Fuente predeterminada con tamaño 36
    try:
        with open("datos.json", "r") as file:
            datos = json.load(file)
            if datos:
                y_offset = 40  # Posición vertical para imprimir cada línea
                for usuario in datos:
                    # Cada dato se convierte en una línea y se renderiza
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
                    y_offset += 30  # Espacio entre los jugadores
    except FileNotFoundError:
        mensaje = font.render("No hay datos guardados para mostrar.", True, BLANCO)
        ventana.blit(mensaje, (40, 30))