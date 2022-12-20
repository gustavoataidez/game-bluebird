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

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Blue Bird')

fundo = pygame.image.load('images/fundo_jogo.png')
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

def is_off_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def get_random_gaiola(xpos):
    tamanho = random.randint(100, 300)
    gaiola = Gaiola(False, xpos, tamanho)
    gaiola_invertido = Gaiola(True, xpos, altura_tela - tamanho - gaiola_gap)
    return (gaiola, gaiola_invertido)

def exibe_mensagem(texto, tamanho, cor, x, y):
        #Exibe um texto na tela do jogo
        fonte = pygame.font.SysFont(FONTE, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        tela.blit(texto, texto_rect)

class Passaro(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.images = [pygame.image.load('images/arara1.png').convert_alpha(),
                    pygame.image.load('images/arara2.png').convert_alpha(),
                    pygame.image.load('images/arara3.png').convert_alpha(),
                    pygame.image.load('images/arara4.png').convert_alpha(),
                    pygame.image.load('images/arara5.png').convert_alpha(),
                    pygame.image.load('images/arara6.png').convert_alpha(),
                    pygame.image.load('images/arara7.png').convert_alpha(),
                    pygame.image.load('images/arara8.png').convert_alpha(),]

        self.velocidade = velocidade

        self.current_image = 0

        self.image = pygame.image.load('images/arara1.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 300
        self.rect[1] = 200

    def update(self):
        self.current_image = (self.current_image + 1) % 8
        self.image = self.images [self.current_image]

        self.velocidade += gravidade

        #update altura
        self.rect[1] += self.velocidade

    def pulo(self):
        self.velocidade = -velocidade