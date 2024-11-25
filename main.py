import pygame, sys
from constantes import *
from blackjack import jugar, mostrar_estadisticas
from otras_funciones_blackjack import *

# Inicialización de Pygame y mixer para audio
pygame.init()
pygame.mixer.init()

# Configuración de la ventana y sonidos del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE_JUEGO)
sonido_crear_baraja = pygame.mixer.Sound("assets/audio/card-fan-1.ogg")
sonido_cartas = pygame.mixer.Sound("assets/audio/card-place-2.ogg")

# Carga de imagenes de fondo y la fuente de texto para el menú
imagenes_cartas= {
    "2_corazones": pygame.image.load("assets/images/cards/PNG/Large/2_corazones.png"),
    "3_corazones": pygame.image.load("assets/images/cards/PNG/Large/3_corazones.png"),
    "4_corazones": pygame.image.load("assets/images/cards/PNG/Large/4_corazones.png"),
    "5_corazones": pygame.image.load("assets/images/cards/PNG/Large/5_corazones.png"),
    "6_corazones": pygame.image.load("assets/images/cards/PNG/Large/6_corazones.png"),
    "7_corazones": pygame.image.load("assets/images/cards/PNG/Large/7_corazones.png"),
    "8_corazones": pygame.image.load("assets/images/cards/PNG/Large/8_corazones.png"),
    "9_corazones": pygame.image.load("assets/images/cards/PNG/Large/9_corazones.png"),
    "10_corazones": pygame.image.load("assets/images/cards/PNG/Large/10_corazones.png"),
    "j_corazones": pygame.image.load("assets/images/cards/PNG/Large/j_corazones.png"),
    "q_corazones": pygame.image.load("assets/images/cards/PNG/Large/q_corazones.png"),
    "k_corazones": pygame.image.load("assets/images/cards/PNG/Large/k_corazones.png"),
    "as_corazones": pygame.image.load("assets/images/cards/PNG/Large/as_corazones.png"),
    #hasta aca corazones
    "2_treboles": pygame.image.load("assets/images/cards/PNG/Large/2_treboles.png"),
    "3_treboles": pygame.image.load("assets/images/cards/PNG/Large/3_treboles.png"),
    "4_treboles": pygame.image.load("assets/images/cards/PNG/Large/4_treboles.png"),
    "5_treboles": pygame.image.load("assets/images/cards/PNG/Large/5_treboles.png"),
    "6_treboles": pygame.image.load("assets/images/cards/PNG/Large/6_treboles.png"),
    "7_treboles": pygame.image.load("assets/images/cards/PNG/Large/7_treboles.png"),
    "8_treboles": pygame.image.load("assets/images/cards/PNG/Large/8_treboles.png"),
    "9_treboles": pygame.image.load("assets/images/cards/PNG/Large/9_treboles.png"),
    "10_treboles": pygame.image.load("assets/images/cards/PNG/Large/10_treboles.png"),
    "j_treboles": pygame.image.load("assets/images/cards/PNG/Large/j_treboles.png"),
    "q_treboles": pygame.image.load("assets/images/cards/PNG/Large/q_treboles.png"),
    "k_treboles": pygame.image.load("assets/images/cards/PNG/Large/k_treboles.png"),
    "as_treboles": pygame.image.load("assets/images/cards/PNG/Large/as_treboles.png"),
    #hasta aca treboles
    "2_diamantes": pygame.image.load("assets/images/cards/PNG/Large/2_diamantes.png"),
    "3_diamantes": pygame.image.load("assets/images/cards/PNG/Large/3_diamantes.png"),
    "4_diamantes": pygame.image.load("assets/images/cards/PNG/Large/4_diamantes.png"),
    "5_diamantes": pygame.image.load("assets/images/cards/PNG/Large/5_diamantes.png"),
    "6_diamantes": pygame.image.load("assets/images/cards/PNG/Large/6_diamantes.png"),
    "7_diamantes": pygame.image.load("assets/images/cards/PNG/Large/7_diamantes.png"),
    "8_diamantes": pygame.image.load("assets/images/cards/PNG/Large/8_diamantes.png"),
    "9_diamantes": pygame.image.load("assets/images/cards/PNG/Large/9_diamantes.png"),
    "10_diamantes": pygame.image.load("assets/images/cards/PNG/Large/10_diamantes.png"),
    "j_diamantes": pygame.image.load("assets/images/cards/PNG/Large/j_diamantes.png"),
    "q_diamantes": pygame.image.load("assets/images/cards/PNG/Large/q_diamantes.png"),
    "k_diamantes": pygame.image.load("assets/images/cards/PNG/Large/k_diamantes.png"),
    "as_diamantes": pygame.image.load("assets/images/cards/PNG/Large/as_diamantes.png"),
    #hasta aca diamantes
    "2_picas": pygame.image.load("assets/images/cards/PNG/Large/2_picas.png"),
    "3_picas": pygame.image.load("assets/images/cards/PNG/Large/3_picas.png"),
    "4_picas": pygame.image.load("assets/images/cards/PNG/Large/4_picas.png"),
    "5_picas": pygame.image.load("assets/images/cards/PNG/Large/5_picas.png"),
    "6_picas": pygame.image.load("assets/images/cards/PNG/Large/6_picas.png"),
    "7_picas": pygame.image.load("assets/images/cards/PNG/Large/7_picas.png"),
    "8_picas": pygame.image.load("assets/images/cards/PNG/Large/8_picas.png"),
    "9_picas": pygame.image.load("assets/images/cards/PNG/Large/9_picas.png"),
    "10_picas": pygame.image.load("assets/images/cards/PNG/Large/10_picas.png"),
    "j_picas": pygame.image.load("assets/images/cards/PNG/Large/j_picas.png"),
    "q_picas": pygame.image.load("assets/images/cards/PNG/Large/q_picas.png"),
    "k_picas": pygame.image.load("assets/images/cards/PNG/Large/k_picas.png"),
    "as_picas": pygame.image.load("assets/images/cards/PNG/Large/as_picas.png"),
    #hasta aca picas
    "parte_atras": pygame.image.load("assets/images/cards/PNG/Large/parte_atras.png")
}

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

# Función para dibujar botones en la pantalla
def dibujar_botones():
    for boton in botones:
        pygame.draw.rect(ventana, boton["color"], boton["rect"])
        texto = font.render(boton["text"], True, NEGRO)
        texto_rect = texto.get_rect(center=boton["rect"].center)
        ventana.blit(texto, texto_rect)

en_pantalla_partidas = False
en_pantalla_como_jugar = False
en_pantalla_valores = False
corriendo = True
datos = mostrar_datos()

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    
    # PARTE DEL MENÚ ------
    MENU_TEXT = font_title.render("BLACKJACK PRIME", True, BLANCO)
    MENU_RECT = MENU_TEXT.get_rect(center=(400, 125))
    ventana.blit(fondo, (0,0))
    ventana.blit(MENU_TEXT, MENU_RECT)
    dibujar_botones()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse_pos = pygame.mouse.get_pos()
            for boton in botones:
                if boton["rect"].collidepoint(mouse_pos):
                    if boton["text"] == "JUGAR":
                        jugar()
                    elif boton["text"] == "COMO JUGAR":
                        en_pantalla_como_jugar = True
                    elif boton["text"] == "VALORES":
                        en_pantalla_valores = True
                    elif boton["text"] == "PARTIDAS":
                        en_pantalla_partidas = True
                    elif boton["text"] == "SALIR":
                        corriendo = False
    
    if en_pantalla_valores:
        # Fondo y texto para la pantalla de valores
        ventana.blit(fondo, (0,0)) 
        valores_cartas = pygame.image.load("assets/images/valores_cartas.png")
        ventana.blit(valores_cartas, (0, 50))
        texto = font.render("ESC para volver al menú principal", True, BLANCO)
        ventana.blit(texto, (0, 565))
        #if que si apretamos la tecla escape nos vuelve al menú principal del juego
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                en_pantalla_valores = False
    
    if en_pantalla_como_jugar:
        ventana.blit(fondo, (0,0))
        como_jugar = pygame.image.load("assets/images/como_jugar.png")
        ventana.blit(como_jugar, (0, 20))
        texto = font.render("ESC para volver al menú principal", True, NEGRO)
        ventana.blit(texto, (0, 565))
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                en_pantalla_como_jugar = False
    
    if en_pantalla_partidas:
        ventana.blit(fondo, (0,0))
        y_offset = 50  
        for linea in datos:
            texto = font.render(linea, True, BLANCO)  
            ventana.blit(texto, (50, y_offset))  
            y_offset += 40  
            texto = font.render("ESC para volver al menú principal", True, BLANCO)
            ventana.blit(texto, (0, 565))
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                en_pantalla_partidas = False
    
    pygame.display.flip()
    pygame.display.update()

pygame.quit()
sys.exit()