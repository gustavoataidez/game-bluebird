import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura_tela = 640
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Blue Bird')

fundo = pygame.image.load('back2 (1).png')
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
    pygame.display.update()

    tela.blit(fundo, (0, 0))