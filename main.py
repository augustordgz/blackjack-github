import pygame 
from constantes import *

pygame.init()
pygame.mixer.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE_JUEGO)
sonido_crear_baraja = pygame.mixer.Sound("assets/audio/card-fan-1.ogg")
sonido_cartas = pygame.mixer.Sound("assets/audio/card-place-2.ogg")

imagenes_cartas= {
    "2_corazones":pygame.image.load("assets/images/cards/PNG/Large/2_corazones.png"),
    
}
fondo = pygame.image.load("assets/images/fondo.jpg")
fuente = pygame.font.Font("assets/fonts/static/PixelifySans-Regular.ttf", 32)

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        
        if evento.type == pygame.KEYDOWN:
            print(f"tecla presionada: {evento.key}")
            if evento.key == pygame.K_SPACE:
                sonido_cartas.set_volume(0.1)
                sonido_cartas.play()
            if evento.key == pygame.K_d:
                pass
            if evento.key == pygame.K_p:
                pass
            if evento.key == pygame.K_q:
                pass
    ventana.blit(fondo, (0,0))
    
    pygame.display.update()

pygame.quit()