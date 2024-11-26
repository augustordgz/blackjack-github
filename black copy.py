import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
ventana = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Colores
VERDE = (0, 128, 0)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Cargar imágenes de las cartas
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

# Crear un mazo completo
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


# Función para mostrar texto en pantalla
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

# Variables iniciales
mano_jugador = [mazo.pop(), mazo.pop()]
mano_croupier = [mazo.pop(), mazo.pop()]
turno_jugador = True
revelar_cartas_croupier = False
resultado = ""

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if turno_jugador:
                if event.key == pygame.K_p:  # Pedir carta
                    mano_jugador.append(mazo.pop())
                    if calcular_valor(mano_jugador) > 21:
                        resultado = "¡Te pasaste! Pierdes."
                        turno_jugador = False
                        revelar_cartas_croupier = True
                if event.key == pygame.K_q:  # Quedarse
                    turno_jugador = False
                    revelar_cartas_croupier = True
            if not turno_jugador and revelar_cartas_croupier:
                # Turno del croupier
                while calcular_valor(mano_croupier) < 17:
                    mano_croupier.append(mazo.pop())
                # Determinar ganador
                valor_jugador = calcular_valor(mano_jugador)
                valor_croupier = calcular_valor(mano_croupier)
                if valor_croupier > 21 or valor_jugador > valor_croupier:
                    resultado = "¡Ganaste!"
                elif valor_jugador < valor_croupier:
                    resultado = "Perdiste."
                else:
                    resultado = "Empate."
    # Dibujar el fondo
    ventana.fill(VERDE)
    # Mostrar las cartas
    mostrar_cartas(mano_jugador, 100, 400)  # Mano del jugador
    mostrar_cartas(mano_croupier, 100, 100, mostrar_segunda=revelar_cartas_croupier)  # Mano del croupier
    # Mostrar valores de las manos
    mostrar_texto(f"Jugador: {calcular_valor(mano_jugador)}", 36, 100, 350)
    if revelar_cartas_croupier:
        mostrar_texto(f"Croupier: {calcular_valor(mano_croupier)}", 36, 100, 50)
    # Mostrar el resultado
    if resultado:
        mostrar_texto(resultado, 48, WIDTH // 2 - 100, HEIGHT // 2 - 50, BLANCO)
    # Mostrar instrucciones
    if turno_jugador and not resultado:
        mostrar_texto("Presiona P para pedir carta, Q para quedarte", 24, 100, 550)
    pygame.display.flip()

pygame.quit()
