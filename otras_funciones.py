import os
import json
import pygame
from constantes import GRIS, NEGRO, BLANCO

# Definicion de colores y botones del menu
botones = [
    {"text": "JUGAR", "rect": pygame.Rect(150, 200, 200, 50), "color": GRIS},
    {"text": "COMO JUGAR", "rect": pygame.Rect(450, 200, 200, 50), "color": GRIS},
    {"text": "VALORES", "rect": pygame.Rect(150, 300, 200, 50), "color": GRIS},
    {"text": "PARTIDAS", "rect": pygame.Rect(450, 300, 200, 50), "color": GRIS},
    {"text": "SALIR", "rect": pygame.Rect(300, 400, 200, 50), "color": GRIS},
]

botones_blackjack = [
    {"text": "DOBLAR", "rect": pygame.Rect(30, 100, 150, 50), "color": GRIS},
    {"text": "PEDIR", "rect": pygame.Rect(30, 200, 150, 50), "color": GRIS},
    {"text": "QUEDARSE", "rect": pygame.Rect(30, 300, 150, 50), "color": GRIS}
]

# Funciones para dibujar botones en la pantalla
def dibujar_botones():
    from main import ventana, font
    """
    |Dibuja un conjunto de botones en la ventana principal usando Pygame.
    |Argumentos:
        None: Esta funcion no recibe argumentos directamente. Depende de variables globales como `botones`, `ventana`, `font` y `NEGRO`.
    |Retorna:
        None: La funcion no devuelve ningun valor. Los botones se renderizan directamente en la ventana.
    """
    for boton in botones:
        pygame.draw.rect(ventana, boton["color"], boton["rect"])
        texto = font.render(boton["text"], True, NEGRO)
        texto_rect = texto.get_rect(center=boton["rect"].center)
        ventana.blit(texto, texto_rect)

def dibujar_botones_blackjack():
    from main import ventana, font
    """
    |Dibuja un conjunto de botones especificos para el modo Blackjack en la ventana principal usando Pygame.
    |Argumentos:
        None: Esta funcion no recibe argumentos directamente. Depende de variables globales como `botones_blackjack`, `ventana`, `font` y `NEGRO`.
    |Retorna:
        None: La funcion no devuelve ningun valor. Los botones se renderizan directamente en la ventana.
    """
    for boton in botones_blackjack:
        pygame.draw.rect(ventana, boton["color"], boton["rect"])
        texto2 = font.render(boton["text"], True, NEGRO)
        texto_rect2 = texto2.get_rect(center=boton["rect"].center)
        ventana.blit(texto2, texto_rect2)

def mostrar_texto(texto, tamaño, x, y):
    from main import ventana
    """
    |Muestra un texto en la ventana de Pygame en una posicion especifica.
    |Argumentos:
        texto (str): El texto que se desea mostrar.
        tamaño (int): El tamaño de la fuente del texto.
        x (int): La coordenada X donde se posicionara el texto.
        y (int): La coordenada Y donde se posicionara el texto.
    |Retorna:
        None: La funcion no devuelve ningun valor. El texto se renderiza directamente en la ventana de Pygame.
    """
    fuente = pygame.font.Font("assets/fonts/static/PixelifySans-Medium.ttf", tamaño)
    superficie_texto = fuente.render(texto, True, BLANCO)
    ventana.blit(superficie_texto, (x, y))

def cargar_jugadores():
    """
    |Carga los datos de los jugadores desde un archivo JSON.
    |Argumentos:
        None: La funcion no requiere argumentos.
    |Retorna:
        dict: Un diccionario con los datos de los jugadores si el archivo "datos.json" existe, retorna un diccionario vacio si el archivo no se encuentra.
    """
    if os.path.exists("datos.json"):
            with open("datos.json", "r") as file:
                return json.load(file)
    return {}