import pygame
import random
import time

largura = 640
altura = 480

pygame.display.set_caption("Reciclagem")
pygame.display.set_icon(pygame.image.load("imagens/lixeira.png"))

display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("imagens/fundo.png")
lixeira = pygame.image.load("imagens/lixeira.png")
latinha = pygame.image.load("imagens/latinha.png")
garrafa = pygame.image.load("imagens/garrafa.png")
pneu = pygame.image.load("imagens/pneu.png")

preto = (0, 0, 0)
branco = (255, 255, 255)

def jogo():
    pygame.init()

    lixeira_posicaoX = largura * 0.45
    lixeira_posicaoY = altura * 0.8
    lixeira_largura = 50
    movimentoX = 0

    latinhaPosicaoX = random.randrange(0, largura - 60)
    latinhaPosicaoY = -30
    latinhaLargura = 20
    latinhaAltura = 30 
    latinhaVelocidade = 5

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10 
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        display.blit(fundo, (0, 0))
        lixeira_posicaoX = lixeira_posicaoX + movimentoX

        if lixeira_posicaoX < 0:
            lixeira_posicaoX = 0
        elif lixeira_posicaoX > 640:
            lixeira_posicaoX = 640
    
    
        display.blit(lixeira, (lixeira_posicaoX, lixeira_posicaoY))
        display.blit(latinha, (latinhaPosicaoX, latinhaPosicaoY))
        
        latinhaPosicaoY = latinhaPosicaoY + latinhaVelocidade
        if latinhaPosicaoY > altura:
            latinhaPosicaoY = -30
            latinhaPosicaoX = random.randrange(0, largura - 30)
        
        if lixeira_posicaoY < latinhaPosicaoY + latinhaAltura:
            if lixeira_posicaoX < latinhaPosicaoX and lixeira_posicaoX + lixeira_largura > latinhaPosicaoX or latinhaPosicaoX + latinhaLargura > lixeira_posicaoX and latinhaPosicaoX + latinhaLargura < lixeira_posicaoX + lixeira_largura:
                latinhaPosicaoY = -30
                latinhaPosicaoX = random.randrange(0, largura - 50)

        pygame.display.update()
        fps.tick(60)
jogo()
print("Volte sempre...")  
