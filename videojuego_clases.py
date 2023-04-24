import pygame, sys
from pygame.locals import *
#variables globales
ancho = 1280
alto = 720
verde = (0, 255, 0)
negro = (0, 0, 0)
#SuperClase Personaje
class personaje(pygame.sprite.Sprite):
    def __init__(self, escala, velocidad_x, velocidad_y, Direccion, P_Vida, P_Aguante, Ataque, Defensa, Vivo, Dialogo):
        self.escala=escala
        abajo = pygame.image.load('Imagenes/abajo.png')
        self.abajo = pygame.transform.scale(abajo,(int(abajo.get_width()*self.escala),int(abajo.get_height()*self.escala)))
        self.rect = self.abajo.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto/2
        self.velocidad_x = velocidad_x#Numerico
        self.velocidad_y = velocidad_y
        self.PV = P_Vida#Numerico
        self.PA = P_Aguante#Numerico
        self.AT = Ataque#Numerico
        self.DEF = Defensa#Numerico
        self.DIR = Direccion#String
        self.DIA = Dialogo#Booleano
        self.LIFE=Vivo#Booleano
        #Numerico constante

        
    def estado(self):
        #print("Vida: ", self.PV, "\nAguante: ", self.PA, "\nAtaque: ", self.AT, "\nDefensa: ", self.DEF)
        print("posx: ", self.pos_x, "\nposy: ", self.pos_y, "\nvelx", self.vel_x, "\nvely", self.vel_y, "\nDireccion:", self.DIR, "\nDialogo: ", self.DIA, "\nVivo: ", self.LIFE)

    def limites(self):
        if self.LIFE == True:
            if self.rect.left<=0:
                self.rect.left = 0
            elif self.rect.right>=1280:
                self.rect.right = 1280
            elif self.rect.top>=590:
                self.rect.top=590
            elif self.rect.bottom<=130:
                self.rect.bottom = 130

    def golpear(self, AG):
        AT=self.AT
        self.PA=self.PA-AG
        return AT
    
    def golpe(self, AR):
        DEF= self.DEF
        if AR>DEF:
            AR=AR-DEF
            self.PV=self.PV-AR
        else:
            print("No has recibido daño")

    def Muerte(self):
        self.PV=0
        self.LIFE = False
        print("has muerto")

    def dibujar(self, superficie):
        superficie.blit(self.abajo, self.rect)
        
#clase enemigo
class enemigo:
    def __init__(self):
        self.persecucion = False
        self.batalla = False
#Subclases de Personaje
class Pacifico(personaje):
    pass
    
class Hostil(personaje, enemigo):
    
    def perseguir(self):
        self.persecucion = True
        print("Te han visto")

    def batalla(self):
        self.batalla = True
        print("Te han pillado!")


#Clase arma
class Arma():
    def __init__(self, Tipo, Alcance, Ataque, ANCHO, ALTO):
        self.Type=Tipo#String
        self.AT = Ataque#Numerico
        self.ALC=Alcance#Numerico
        self.ANCHO=ANCHO#Numerico
        self.ALTO=ALTO#Numerico
        self.AC=golpe#Booleano
enjuego = True
def Juego():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Juego")
    jugador = personaje(0.3,0,0,"izquierda",100,100,50,50,True,False)
    
    while True:
        jugador.limites()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if enjuego == True:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        jugador.velocidad_x = -1
                    if evento.key == pygame.K_RIGHT:
                        jugador.velocidad_x = 1
                    if evento.key == pygame.K_DOWN:
                        jugador.velocidad_y = 1
                    if evento.key == pygame.K_UP:
                        jugador.velocidad_y = -1
                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT:
                        jugador.velocidad_x = 0
                    if evento.key == pygame.K_RIGHT:
                        jugador.velocidad_x = 0
                    if evento.key == pygame.K_DOWN:
                        jugador.velocidad_y = 0
                    if evento.key == pygame.K_UP:
                        jugador.velocidad_y = 0
        ventana.fill(negro)
        jugador.rect.right += jugador.velocidad_x
        jugador.rect.top += jugador.velocidad_y
        jugador.dibujar(ventana)
        pygame.display.update()

Juego()

