import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura_tela = 640
altura_tela = 480
velocidade = 10
gravidade = 1
velocidadejogo = 10

class Passaro(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.images = [pygame.image.load('testeupflap.png').convert_alpha(),
                       pygame.image.load('testemidflap.png').convert_alpha(),
                       pygame.image.load('testedownflap.png').convert_alpha()]

        self.velocidade = velocidade

        self.current_image = 0

        self.image = pygame.image.load('testeupflap.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = largura_tela / 2
       
        self.rect[1] = altura_tela / 2
    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images [self.current_image]

        self.velocidade += gravidade

        #update altura
        self.rect[1] += self.velocidade

    def pulo(self):
        self.velocidade = -velocidade
class base(pygame.sprite.Sprite):

    def __init__(self, largura, altura):
        pygame.sprite.Sprite. __init__(self)

        self.image = pygame.image.load('chãofinal.png')
        self.image = pygame.transform.scale(self.image, (largura, altura))

        self.rect = self.image.get_rect()
        self.rect[1] = altura_tela - altura

    def update(self):
        self.rect[0] -= velocidadejogo


tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Blue Bird')

fundo = pygame.image.load('imagem de fundo.png')
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

grupopassaro = pygame.sprite.Group()
passaro = Passaro()
grupopassaro.add(passaro)

base_base = pygame.sprite.Group()
base = base(2 * largura_tela, 80)
base_base.add(base)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
        if event.type == KEYDOWN:
              if event.key == K_SPACE:
                passaro.pulo()  
    tela.blit(fundo, (0, 0))
    
    grupopassaro.update()
    base_base.update()

    grupopassaro.draw(tela)
    base_base.draw(tela)

    pygame.display.update()