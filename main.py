import sys
import random
import pygame
from constantes import *
from otras_funciones import *
from guardar_y_cargar import *
from funciones_menu import mostrar_como_jugar, mostrar_partidas, mostrar_valores

partidas_jugadas = 0
partidas_ganadas = 0
partidas_perdidas = 0
empates = 0
corriendo = True
turno_jugador = True
revelar_cartas_croupier = False
resultado = ""

# Inicializacion de Pygame y mixer para audio
pygame.init()
pygame.mixer.init()

# Configuracion de la ventana y sonidos del juego
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE_JUEGO)

pygame.mixer.music.load("assets/audio/CASINO Jazz Music #1.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(1)

sonido_crear_baraja = pygame.mixer.Sound("assets/audio/card-fan-1.ogg")
sonido_crear_baraja.set_volume(0.1)
sonido_cartas = pygame.mixer.Sound("assets/audio/card-place-2.ogg")
sonido_cartas.set_volume(0.1)

# Carga de imagenes de fondo y la fuente de texto para el menu
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

# Función para calcular el valor de una mano
def calcular_valor(mano):
    """
    |Calcula el valor total de la mano de cartas.
    |Argumentos:
        mano (list): Lista de cartas representadas como cadenas. Cada carta debe estar en formato abreviado.
    |Retorna:
        int: El valor total de la mano:
            - Figuras (J, Q, K) valen 10.
            - Ases valen inicialmente 11, pero pueden ajustarse a 1 si 
            el valor total de la mano supera 21.
            - Cartas numericas tienen su valor numerico.
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
                valor += int(carta[:-1])  # Cartas numericas (ejemplo: "2C" -> 2)
            except ValueError:
                print(f"Error al interpretar la carta: {carta}")
    # Ajustar los Ases si el valor total excede 21
    while valor > 21 and ases > 0:
        valor -= 10
        ases -= 1
    return valor

# Función para mostrar cartas
def mostrar_cartas(mano, x_inicio, y, mostrar_segunda=True):
    """
    |Muestra las cartas de la mano del jugador y del croupier.
    |Argumentos:
        mano (list): Lista de cartas representadas como cadenas. Cada carta corresponde a una clave en `imagenes_cartas`.
        x_inicio (int): Coordenada X inicial para posicionar las cartas.
        i (int): Coordenada Y donde se mostraran las cartas.
        mostrar_segunda (bool): Si es True, muestra todas las cartas. Si es False, oculta la segunda carta.
    |Retorna:
        None: La funcion no devuelve ningun valor. Las cartas se renderizan directamente en la ventana de Pygame.
    """
    for i, carta in enumerate(mano):
        if i == 1 and not mostrar_segunda:  # No mostrar la segunda carta del croupier
            ventana.blit(reverso_carta, (x_inicio + i * 100, y))
        else:
            ventana.blit(imagenes_cartas[carta], (x_inicio + i * 100, y))

def ingresar_usuario():
    """
    |Permite al usuario ingresar su nombre mediante una interfaz gráfica con Pygame.
    |Argumentos:
        None: La función no requiere argumentos. Depende de variables globales como `ventana`, `fondo`, y `BLANCO`.
    |Retorna:
        str: El nombre ingresado por el usuario, siempre que sea válido (no esté vacío y no esté repetido en los datos de jugadores previamente cargados).
    """
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

def mostrar_juego(nombre=None):
    global partidas_jugadas, partidas_ganadas, partidas_perdidas, empates
    # Si el nombre no se proporciona, pedirlo
    if not nombre:
        nombre = ingresar_usuario()
    sonido_crear_baraja.play()
    while True:  # Bucle principal para jugar varias partidas
        # Inicializar manos y barajar el mazo
        mazo = list(cartas.keys())
        random.shuffle(mazo)
        mano_jugador = [mazo.pop(), mazo.pop()]
        mano_croupier = [mazo.pop(), mazo.pop()]
        turno_jugador = True
        revelar_cartas_croupier = False
        resultado = ""
        while True:  # Bucle para la partida actual
            ventana.blit(fondo, (0, 0))  # Fondo del juego
            # Mostrar manos de jugador y croupier
            mostrar_cartas(mano_jugador, 200, 400)  # Mano del jugador
            mostrar_cartas(mano_croupier, 200, 100, mostrar_segunda=revelar_cartas_croupier)  # Mano del croupier
            # Mostrar valores de las manos
            valor_jugador = calcular_valor(mano_jugador)
            valor_croupier = calcular_valor(mano_croupier)
            mostrar_texto(f"{nombre}: {valor_jugador}", 30, 200, 370)
            if revelar_cartas_croupier:
                mostrar_texto(f"Croupier: {valor_croupier}", 30, 200, 70)
            else:
                mostrar_texto("Croupier: ?", 30, 200, 70)
            # Mostrar resultado si el juego termina
            if resultado:
                mostrar_texto(resultado, 20, 200, 250)
                mostrar_texto("Presione 'Enter' para otra partida o 'Escape' para salir", 20, 200, 300)
            # Dibujar botones
            dibujar_botones_blackjack()
            pygame.display.flip()
            # Manejo de eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if resultado:  # Si el juego terminó
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_RETURN:  # Nueva partida
                            return mostrar_juego(nombre)  # Iniciar otra partida con el mismo nombre
                        elif evento.key == pygame.K_ESCAPE:  # Volver al menú
                            # Cuando llames a guardar_partida:
                            guardar_partida(nombre, partidas_jugadas, partidas_ganadas, partidas_perdidas, empates)     
                            return  # Salir de la función y regresar al menú principal
                elif turno_jugador and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    for boton in botones_blackjack:
                        if boton["rect"].collidepoint(mouse_pos):
                            if boton["text"] == "DOBLAR":
                                mano_jugador.append(mazo.pop())
                                valor_jugador = calcular_valor(mano_jugador)
                                turno_jugador = False
                                break
                            elif boton["text"] == "PEDIR":
                                mano_jugador.append(mazo.pop())
                                valor_jugador = calcular_valor(mano_jugador)
                                sonido_cartas.play()
                                if valor_jugador > 21:  # Si el jugador se pasa
                                    resultado = f"{nombre} pierde, te pasaste de 21."
                                    partidas_jugadas += 1
                                    partidas_perdidas += 1
                                    revelar_cartas_croupier = True
                                break
                            elif boton["text"] == "QUEDARSE":
                                turno_jugador = False
                                break
            # Lógica del turno del croupier
            if not turno_jugador and not resultado:
                revelar_cartas_croupier = True
                while calcular_valor(mano_croupier) < 17:  # El croupier pide si tiene menos de 17
                    mano_croupier.append(mazo.pop())
                    sonido_cartas.play()
                valor_croupier = calcular_valor(mano_croupier)
                # Determinar el resultado
                if valor_croupier > 21:
                    resultado = f"{nombre} gana, el croupier se pasó."
                    partidas_jugadas += 1
                    partidas_ganadas += 1
                elif valor_jugador > valor_croupier:
                    resultado = f"{nombre} gana, tiene más puntos que el croupier."
                    partidas_jugadas += 1
                    partidas_ganadas += 1
                elif valor_croupier == valor_jugador:
                    resultado = "Empate."
                    partidas_jugadas += 1
                    empates += 1
                else:
                    resultado = f"{nombre} pierde, el croupier tiene más puntos."
                    partidas_jugadas += 1
                    partidas_perdidas += 1

while corriendo:
    MENU_TEXTO = font_title.render("BLACKJACK PRIME", True, BLANCO)
    MENU_RECT = MENU_TEXTO.get_rect(center=(400, 125))
    ventana.blit(fondo, (0, 0))
    ventana.blit(MENU_TEXTO, MENU_RECT)
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