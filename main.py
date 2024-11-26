import sys
import os
import random
import pygame
from constantes import *
from blackjack import jugar
from otras_funciones_blackjack import *

# Inicialización de Pygame y mixer para audio
pygame.init()
pygame.mixer.init()

# Configuración de la ventana y sonidos del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE_JUEGO)

pygame.mixer.music.load("assets/audio/CASINO Jazz Music #1.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(1)

sonido_crear_baraja = pygame.mixer.Sound("assets/audio/card-fan-1.ogg")
sonido_crear_baraja.set_volume(0.1)
sonido_cartas = pygame.mixer.Sound("assets/audio/card-place-2.ogg")
sonido_cartas.set_volume(0.1)

# Carga de imagenes de fondo y la fuente de texto para el menú
cartas = {
    "2C": "assets/images/cards/PNG/Large/2_corazones.png",
    "3C": "assets/images/cards/PNG/Large/3_corazones.png",
    "4C": "assets/images/cards/PNG/Large/4_corazones.png",
    "5C": "assets/images/cards/PNG/Large/5_corazones.png",
    "6C": "assets/images/cards/PNG/Large/6_corazones.png",
    "7C": "assets/images/cards/PNG/Large/7_corazones.png",
    "8C": "assets/images/cards/PNG/Large/8_corazones.png",
    "9C": "assets/images/cards/PNG/Large/9_corazones.png",
    "10C": "assets/images/cards/PNG/Large/10_corazones.png",
    "JC": "assets/images/cards/PNG/Large/j_corazones.png",
    "QC": "assets/images/cards/PNG/Large/q_corazones.png",
    "KC": "assets/images/cards/PNG/Large/k_corazones.png",
    "AC": "assets/images/cards/PNG/Large/as_corazones.png",
    "2T": "assets/images/cards/PNG/Large/2_treboles.png",
    "3T": "assets/images/cards/PNG/Large/3_treboles.png",
    "4T": "assets/images/cards/PNG/Large/4_treboles.png",
    "5T": "assets/images/cards/PNG/Large/5_treboles.png",
    "6T": "assets/images/cards/PNG/Large/6_treboles.png",
    "7T": "assets/images/cards/PNG/Large/7_treboles.png",
    "8T": "assets/images/cards/PNG/Large/8_treboles.png",
    "9T": "assets/images/cards/PNG/Large/9_treboles.png",
    "10T": "assets/images/cards/PNG/Large/10_treboles.png",
    "JT": "assets/images/cards/PNG/Large/j_treboles.png",
    "QT": "assets/images/cards/PNG/Large/q_treboles.png",
    "KT": "assets/images/cards/PNG/Large/k_treboles.png",
    "AT": "assets/images/cards/PNG/Large/as_treboles.png",
    "2D": "assets/images/cards/PNG/Large/2_diamantes.png",
    "3D": "assets/images/cards/PNG/Large/3_diamantes.png",
    "4D": "assets/images/cards/PNG/Large/4_diamantes.png",
    "5D": "assets/images/cards/PNG/Large/5_diamantes.png",
    "6D": "assets/images/cards/PNG/Large/6_diamantes.png",
    "7D": "assets/images/cards/PNG/Large/7_diamantes.png",
    "8D": "assets/images/cards/PNG/Large/8_diamantes.png",
    "9D": "assets/images/cards/PNG/Large/9_diamantes.png",
    "10D": "assets/images/cards/PNG/Large/10_diamantes.png",
    "JD": "assets/images/cards/PNG/Large/j_diamantes.png",
    "QD": "assets/images/cards/PNG/Large/q_diamantes.png",
    "KD": "assets/images/cards/PNG/Large/k_diamantes.png",
    "AD": "assets/images/cards/PNG/Large/as_diamantes.png",
    "2P":  "assets/images/cards/PNG/Large/2_picas.png",
    "3P":  "assets/images/cards/PNG/Large/3_picas.png",
    "4P":  "assets/images/cards/PNG/Large/4_picas.png",
    "5P":  "assets/images/cards/PNG/Large/5_picas.png",
    "6P":  "assets/images/cards/PNG/Large/6_picas.png",
    "7P":  "assets/images/cards/PNG/Large/7_picas.png",
    "8P":  "assets/images/cards/PNG/Large/8_picas.png",
    "9P":  "assets/images/cards/PNG/Large/9_picas.png",
    "10P": "assets/images/cards/PNG/Large/10_picas.png",
    "JP":  "assets/images/cards/PNG/Large/j_picas.png",
    "QP":  "assets/images/cards/PNG/Large/q_picas.png",
    "KP":  "assets/images/cards/PNG/Large/k_picas.png",
    "AP": "assets/images/cards/PNG/Large/as_picas.png"
}
imagenes_cartas = {clave: pygame.image.load(ruta) for clave, ruta in cartas.items()}
reverso_carta = pygame.image.load("assets/images/cards/PNG/Large/parte_atras.png")  # Imagen para la carta volteada

fondo = pygame.image.load("assets/images/fondo.jpg")
font = pygame.font.Font("assets/fonts/static/PixelifySans-Regular.ttf", 30)
font_title = pygame.font.Font("assets/fonts/static/PixelifySans-Regular.ttf", 72)

# Definición de colores y botones del menú
botones = [
    {"text": "JUGAR", "rect": pygame.Rect(150, 200, 200, 50), "color": GRIS},
    {"text": "COMO JUGAR", "rect": pygame.Rect(450, 200, 200, 50), "color": GRIS},
    {"text": "VALORES", "rect": pygame.Rect(150, 300, 200, 50), "color": GRIS},
    {"text": "PARTIDAS", "rect": pygame.Rect(450, 300, 200, 50), "color": GRIS},
    {"text": "SALIR", "rect": pygame.Rect(300, 400, 200, 50), "color": GRIS},
]

botones_blackjack = [
    {"text": "DOBLAR", "rect": pygame.Rect(70, 100, 150, 50), "color": GRIS},
    {"text": "PEDIR", "rect": pygame.Rect(70, 200, 150, 50), "color": GRIS},
    {"text": "QUEDARSE", "rect": pygame.Rect(70, 300, 150, 50), "color": GRIS},
    {"text": "SALIR", "rect": pygame.Rect(70, 400, 150, 50), "color": GRIS}
]

# Funciones para dibujar botones en la pantalla
def dibujar_botones():
    for boton in botones:
        pygame.draw.rect(ventana, boton["color"], boton["rect"])
        texto = font.render(boton["text"], True, NEGRO)
        texto_rect = texto.get_rect(center=boton["rect"].center)
        ventana.blit(texto, texto_rect)

def dibujar_botones_blackjack():
    for boton in botones_blackjack:
        pygame.draw.rect(ventana, boton["color"], boton["rect"])
        texto2 = font.render(boton["text"], True, NEGRO)
        texto_rect2 = texto2.get_rect(center=boton["rect"].center)
        ventana.blit(texto2, texto_rect2)


mazo = list(cartas.keys()) * 4  # Cada carta aparece 4 veces
random.shuffle(mazo)

# Función para calcular el valor de una mano
def calcular_valor(mano):
    """
    Calcula el valor total de una mano en Blackjack.
    :param mano: Lista de cartas (ejemplo: ["2C", "AP", "RD"]).
    :return: Valor total de la mano.
    """
    valor = 0
    ases = 0
    for carta in mano:
        if carta[0] in "JQK":  # Figuras (J, Q, K) valen 10
            valor += 10
        elif carta[0] == "A":  # Ases inicialmente valen 11
            valor += 11
            ases += 1
        else:
            try:
                valor += int(carta[:-1])  # Cartas numéricas (ejemplo: "2C" -> 2)
            except ValueError:
                print(f"Error al interpretar la carta: {carta}")
    # Ajustar los Ases si el valor total excede 21
    while valor > 21 and ases > 0:
        valor -= 10
        ases -= 1
    return valor

def mostrar_texto(texto, tamaño, x, y, color=BLANCO):
    fuente = pygame.font.Font(None, tamaño)
    superficie_texto = fuente.render(texto, True, color)
    ventana.blit(superficie_texto, (x, y))

# Función para mostrar cartas
def mostrar_cartas(mano, x_inicio, y, mostrar_segunda=True):
    for i, carta in enumerate(mano):
        if i == 1 and not mostrar_segunda:
            ventana.blit(reverso_carta, (x_inicio + i * 100, y))
        else:
            ventana.blit(imagenes_cartas[carta], (x_inicio + i * 100, y))


# Definición de variables que se utilizan para las diferentes pantallas
corriendo = True
datos = mostrar_datos()
mano_jugador = [mazo.pop(), mazo.pop()]
mano_croupier = [mazo.pop(), mazo.pop()]
turno_jugador = True
revelar_cartas_croupier = False
resultado = ""

def cargar_jugadores():
    if os.path.exists("datos.json"):
        with open("datos.json", "r") as file:
            return json.load(file)
    return {}

def ingresar_usuario():
    jugadores = cargar_jugadores()
    font = pygame.font.Font("assets/fonts/static/PixelifySans-Medium.ttf", 36)
    nombre = ""
    
    while True:
        ventana.blit(fondo, (0,0))
        texto_ingresar = font.render("Ingrese su nombre:", True, BLANCO)
        texto_nombre = font.render(nombre, True, BLANCO)
        
        ventana.blit(texto_ingresar, (100, 200))
        ventana.blit(texto_nombre, (450, 200))
        
        pygame.display.flip()  # Asegurar que la pantalla se actualice
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Confirmar con Enter
                    if nombre and nombre not in jugadores:
                        return nombre
                elif evento.key == pygame.K_BACKSPACE:  # Borrar último carácter
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode  # Agregar caracteres


def mostrar_valores():
    while True:
        ventana.blit(fondo, (0, 0))
        valores_cartas = pygame.image.load("assets/images/valores_cartas.png")
        ventana.blit(valores_cartas, (0, 50))
        texto = font.render("ESC para volver al menú principal", True, BLANCO)
        ventana.blit(texto, (0, 565))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

def mostrar_como_jugar():
    while True:
        ventana.blit(fondo, (0, 0))
        como_jugar = pygame.image.load("assets/images/como_jugar.png")
        ventana.blit(como_jugar, (0, 20))
        texto = font.render("ESC para volver al menú principal", True, NEGRO)
        ventana.blit(texto, (0, 565))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

def mostrar_partidas():
    while True:
        ventana.blit(fondo, (0, 0))
        y_offset = 50
        for linea in datos:
            texto = font.render(linea, True, BLANCO)
            ventana.blit(texto, (50, y_offset))
            y_offset += 40
        texto = font.render("ESC para volver al menú principal", True, BLANCO)
        ventana.blit(texto, (0, 565))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

def mostrar_juego():
    nombre = ingresar_usuario()  # Pedir el nombre del usuario
    while True:
        ventana.blit(fondo, (0, 0))
        dibujar_botones_blackjack()
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for boton in botones_blackjack:
                    if boton["rect"].collidepoint(mouse_pos):
                        if boton["text"] == "DOBLAR":
                            print(f"{nombre} seleccionó DOBLAR")
                        elif boton["text"] == "PEDIR":
                            print(f"{nombre} seleccionó PEDIR")
                        elif boton["text"] == "QUEDARSE":
                            print(f"{nombre} seleccionó QUEDARSE")
                        elif boton["text"] == "SALIR":
                            return




while corriendo:
    MENU_TEXT = font_title.render("BLACKJACK PRIME", True, BLANCO)
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 125))
    ventana.blit(fondo, (0, 0))
    ventana.blit(MENU_TEXT, MENU_RECT)
    dibujar_botones()
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  
            mouse_pos = pygame.mouse.get_pos()
            for boton in botones:
                if boton["rect"].collidepoint(mouse_pos):
                    if boton["text"] == "JUGAR":
                        mostrar_juego()  
                    elif boton["text"] == "COMO JUGAR":
                        mostrar_como_jugar()
                    elif boton["text"] == "VALORES":
                        mostrar_valores()
                    elif boton["text"] == "PARTIDAS":
                        mostrar_partidas()
                    elif boton["text"] == "SALIR":
                        corriendo = False
    pygame.display.flip()

pygame.quit()
sys.exit()