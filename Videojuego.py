import pygame, sys
from pygame.locals import *
#variables globales
ancho = 900
alto = 400
class personaje(pygame.sprite.Sprite):
    """clase para los personaje"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.abajo = pygame.image.load('Imagenes/abajo.png')
        self.rect = self.abajo.get_rect()
        self.rect.centerx = ancho/
        self.rect.centery = alto/2

        self.Vida=True
    def dibujar(self, superficie):
        superficie.blit(self.abajo, self.rect)
        
def Juego():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Juego")
    ventana.fill("VERDE")

    jugador = personaje()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
                
        jugador.dibujar(ventana)
        pygame.display.update()

Juego()
