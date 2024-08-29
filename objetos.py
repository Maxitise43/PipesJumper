import pygame

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 80
        self.alto = 60
        self.velocidad = 0
        self.gravedad = 0.5
        self.color = "orange"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.salto = True
        self.rotacion = 0
        self.imagen = pygame.image.load("C:/Users/maxit/Documents/Visual Studio Code/bird.png")
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho, self.alto))
        
    def Dibujar(self, ventana):
        
        self.rect = pygame.Rect(self.x + 5, self.y + 5, self.ancho - 10, self.alto - 10)
        self.imagen = pygame.transform.rotate(self.imagen, self.rotacion)
        ventana.blit(self.imagen, (self.x, self.y))
    
    def Velocidad(self):
        if((self.y <= 720 - self.alto and self.y >= 0) or self.velocidad < 0):
            self.velocidad += self.gravedad
            self.y += self.velocidad
        if(self.y <= 0):
            self.y = 0
            self.velocidad = 0
            return True
        if(self.y >= (720 - self.alto)):
            self.y = 720 - self.alto
            self.velocidad = 0
            return True
        return False

    def Saltar(self):
        TECLAS = pygame.key.get_pressed()
        
        if((TECLAS[pygame.K_w] or TECLAS[pygame.K_SPACE] or TECLAS[pygame.K_UP]) and self.salto ):
            self.velocidad = -10
            self.salto = False
        elif(TECLAS[pygame.K_w] == False and TECLAS[pygame.K_SPACE] == False and TECLAS[pygame.K_UP] == False):
            self.salto = True

class Pipe:
    
    def __init__(self, x, lh, h):
        self.x = x
        self.ancho = 100
        self.alturaSup = h
        self.alturaInf = lh
        self.velocidad = 3
        self.color = "green"
        self.cruzada = False
        self.imagen = pygame.image.load("C:/Users/maxit/Documents/Visual Studio Code/pipe.png")
        
    def Dibujar(self, ventana):
        self.rectSup = pygame.Rect(self.x, 0, self.ancho, 0 + self.alturaSup)
        self.rectInf = pygame.Rect(self.x, self.alturaInf, self.ancho, 720 - self.alturaSup)
        self.imagen = pygame.transform.rotate(self.imagen, 180)
        ventana.blit(self.imagen, (self.x, self.alturaInf))
        self.imagen = pygame.transform.rotate(self.imagen, 180)
        ventana.blit(self.imagen, (self.x, self.alturaSup - self.imagen.get_height()))
        
        
        
    def Velocidad(self):
        if(self.x < -self.ancho):
            return True
        else:
            self.x -= self.velocidad
            return False

class BGrond:
    def __init__(self, y, ancho):
        self.Fx = 0
        self.Mx = 0
        self.y = y
        self.Fimagen = pygame.image.load("C:/Users/maxit/Documents/Visual Studio Code/FrontBackGround.png")
        self.Mimagen = pygame.image.load("C:/Users/maxit/Documents/Visual Studio Code/MiddBackGround.png")
        self.Bimagen = pygame.image.load("C:/Users/maxit/Documents/Visual Studio Code/BackBackGround.png")
        self.Fimagen = pygame.transform.scale(self.Fimagen, (ancho + 5, 400))
        self.Mimagen = pygame.transform.scale(self.Mimagen, (ancho + 5, 640))
        self.Bimagen = pygame.transform.scale(self.Bimagen, (ancho + 200, 640))
                     
    def Velocidad(self):
        self.Fx -= 1.5
        self.Mx -= 0.75
        
        if(self.Fx < -self.Fimagen.get_width()):
            self.Fx = self.Fimagen.get_width()
        if(self.Mx < -self.Mimagen.get_width()):
            self.Mx = self.Mimagen.get_width()
        
    def DibujarPrimerFondo(self, ventana):
        ventana.blit(self.Bimagen, (0, 0))
    
    def DibujarSegundoFondo(self, ventana):
        ventana.blit(self.Mimagen, (self.Mx, self.y - self.Mimagen.get_height() / 2 - 25))
        
    def DibujarTercerFondo(self, ventana):
        ventana.blit(self.Fimagen, (self.Fx, self.y - self.Fimagen.get_height()))