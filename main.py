import random
import pygame
from Objetos import Bird, Pipe, BGrond
pygame.init()

def main():
    ANCHO = 1280
    ALTO = 720
    FPS = 60
    FUENTE = pygame.font.SysFont("Comic Sans", 40)
    salir = True
    altura = 260
    variacion = 30
    relacion = 4
    dificultad = 1
    bird = Bird(100, ALTO / 2)
    pipes = []
    score = 0
    rango = 3
    
    bg = []
    for i in range(2):
        bg.append(BGrond(ALTO, ANCHO))
        bg[i].Fx = ANCHO * i
        bg[i].Mx = ANCHO * i


    for i in range(4):
        pipes.append(Pipe(500 + 345 * i, altura + 250, altura))
        if(random.randrange(1, rango + 3) <= relacion):
               altura -= variacion
               relacion -= 1
        else:
            altura += variacion
            relacion += 1
    
    VENTANA = pygame.display.set_mode([ANCHO, ALTO])
    RELOJ = pygame.time.Clock()
    
    while(salir):
        
        if(score >= 10 * dificultad and dificultad < 6):
            dificultad += 1
            variacion += 5
            
        if(variacion * (relacion + rango) > ALTO and (relacion + rango) > 2):
            rango -= 1
        
        texto_score = FUENTE.render("Puntaje: " + str(score), True, "white")
        RELOJ.tick(FPS)
        
        EVENTOS = pygame.event.get()
        for EVENTO in EVENTOS:
            if(EVENTO.type == pygame.QUIT):
                salir = False

        VENTANA.fill("cyan")
        #bg[0].DibujarPrimerFondo(VENTANA)
        
        #for bgs in bg:
        #    bgs.DibujarSegundoFondo(VENTANA)
        
        #for bgs in bg:
        #    bgs.DibujarTercerFondo(VENTANA)
        #    bgs.Velocidad()

        if(bird.Velocidad()):
            salir = False
        
        bird.Saltar()
        bird.Dibujar(VENTANA)
        for pipe in pipes:
            pipe.velocidad = 3 * (1 + (score) / 20)
            if(pipe.Velocidad()):
                pipes.pop(0)
                if(random.randrange(1, relacion + 4) <= relacion):
                    altura -= variacion
                    relacion -= 1
                else:
                    altura += variacion
                    relacion += 1
                
                pipes.append(Pipe(ANCHO, altura + 250 - (dificultad - 1) * 10, altura + (dificultad - 1) * 10))
            else:
                pipe.Dibujar(VENTANA)
            
            if(pygame.Rect.colliderect(bird.rect, pipe.rectSup) or pygame.Rect.colliderect(bird.rect, pipe.rectInf)):
                salir = False
            if(bird.x >= pipe.x and not pipe.cruzada):
                score += 1
                pipe.cruzada = True
        VENTANA.blit(texto_score, (10, 5))
        pygame.display.update()
        
    print("Puntaje: ", score, sep = "")
    
    return 0


main()
quit()