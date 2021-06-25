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
lixeira = pygame.imagem.load("imagens/lixeira.png")
latinha = pygame.imagem.load("imagens/latinha.png")
garrafa = pygame.image.load("imagens/garrafa.png")
pneu = pygame.image.load("imagens/pneu.png")

preto = (0, 0, 0)
branco = (255, 255, 255)