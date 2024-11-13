import pygame 
pygame.init()
pygame.mixer.init()

ANCHO = 800
ALTO = 600
NOMBRE_JUEGO = "BLACKJACK Grupo PRIME"
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(NOMBRE_JUEGO)
sonido_cartas = pygame.mixer.Sound("assets/audio/card-fan-1.ogg")

fondo = pygame.image.load("assets/images/fondo.jpg")
fuente = pygame.font.Font(None, 36)

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
    ventana.blit(fondo, (0,0))
    x, y = pygame.mouse.get_pos()
    texto = fuente.render(f"Posicion del mouse: ({x}), ({y})", True, (118,238,198))
    ventana.blit(texto, (120, 20))
    
    pygame.display.update()

pygame.quit()