import pygame, random
from pygame.locals import *

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

FONTE = 'Source Sans Pro Black'
FONTE_TITULO = 'Showcard Gothic'

largura_tela = 640
altura_tela = 480
velocidade = 10
gravidade = 1
velocidade_do_jogo = 10

largura_chao = 2 * largura_tela
altura_chao = 80

largura_gaiola = 70 
altura_gaiola = 280

pontos = 0
pontos += 1
gaiola_gap = 160