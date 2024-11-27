import sys
import pygame
from constantes import BLANCO, NEGRO
from guardar_y_cargar import mostrar_datos_pygame

def mostrar_valores():
    """
    |Muestra la imagen de los valores de las cartas y un mensaje en la ventana de Pygame, la ventana se actualiza hasta que el usuario presiona la tecla ESC para volver al menú principal.
    |Argumentos:
        None: La función no recibe argumentos. Depende de variables globales importadas como `ventana`, `font`, y `fondo` desde el archivo `main`.
    |Retorna:
        None: La función no devuelve ningún valor. La ventana se actualiza con la imagen de los valores de las cartas y el mensaje de "ESC para volver al menú principal". La función termina cuando el usuario presiona la tecla ESC.
    
    """
    from main import ventana, font, fondo
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
    """
    |Muestra la imagen de cómo jugar y un mensaje en la ventana de Pygame. 
    La ventana se actualiza hasta que el usuario presiona la tecla ESC para regresar al menú principal.
    |Argumentos:
        None: La función no recibe argumentos. Depende de variables globales importadas como `ventana`, `font`, `fondo` y `NEGRO` desde el archivo `main`.
    |Retorna:
        None: La función no devuelve ningún valor. La ventana se actualiza con la imagen de cómo jugar y el mensaje de "ESC para volver al menú principal". La función termina cuando el usuario presiona la tecla ESC para regresar al menú principal.
    """
    from main import ventana, font, fondo
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
    """
    |Muestra los datos de las partidas y un mensaje en la ventana de Pygame. 
    La ventana se actualiza hasta que el usuario presiona la tecla ESC para regresar al menú principal.
    |Argumentos:
        None: La función no recibe argumentos. Depende de variables globales importadas  como `ventana`, `font`, `fondo` y la función `mostrar_datos_pygame` desde el archivo `main`.
    |Retorna:
        None: La función no devuelve ningún valor. La ventana se actualiza con los datos de las partidas y el mensaje de "ESC para volver al menú principal". La función termino cuando el usuario presiona la tecla ESC para regresar al menú principal.
    """
    from main import ventana, font, fondo
    while True:
        ventana.blit(fondo, (0, 0))
        mostrar_datos_pygame(ventana) 
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