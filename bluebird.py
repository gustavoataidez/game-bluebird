import pygame, random
from pygame.locals import *
from sys import exit

largura_tela = 640
altura_tela = 480
velocidade = 10
gravidade = 1
velocidadejogo = 10

largurachao = 2 * largura_tela
alturachao = 80

largura_gaiola = 70 
altura_gaiola = 280

gaiola_gap = 200

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
        self.rect[0] = largura_tela / 2
        self.rect[1] = altura_tela / 2

    def update(self):
        self.current_image = (self.current_image + 1) % 8
        self.image = self.images [self.current_image]

        self.velocidade += gravidade

        #update altura
        self.rect[1] += self.velocidade

    def pulo(self):
        self.velocidade = -velocidade

class Gaiola(pygame.sprite.Sprite):
    
    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/gaiola.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (largura_gaiola, altura_gaiola))

        self.rect = self.image.get_rect()
        self.rect[0] = xpos

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else:
            self.rect[1] = altura_tela - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= velocidadejogo

class Chao(pygame.sprite.Sprite):

    def __init__(self, ichao):
        pygame.sprite.Sprite. __init__(self)

        self.image = pygame.image.load('images/chãofinal.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(largurachao, alturachao))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = ichao
        self.rect[1] = altura_tela - alturachao

    def update(self):
        self.rect[0] -= velocidadejogo

def is_off_tela(sprite):
    return sprite.rect[0] < -(sprite.rect[2])

def get_random_gaiola(xpos):
    tamanho = random.randint(100, 300)
    gaiola = Gaiola(False, xpos, tamanho)
    gaiola_invertido = Gaiola(True, xpos, altura_tela - tamanho - gaiola_gap)
    return (gaiola, gaiola_invertido)
 
pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Blue Bird')

fundo = pygame.image.load('images/imagem de fundo 3.png')
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))

grupopassaro = pygame.sprite.Group()
passaro = Passaro()
grupopassaro.add(passaro)

chao_chao = pygame.sprite.Group()
for i in range(2):
    chao = Chao( largurachao * i)
    chao_chao.add(chao)

grupogaiola = pygame.sprite.Group()
for i in range(2):
    gaiola = get_random_gaiola(largura_tela * i + 500) 
    grupogaiola.add(gaiola[0])
    grupogaiola.add(gaiola[1])

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

    if is_off_tela(chao_chao.sprites()[0]):
        chao_chao.remove(chao_chao.sprites()[0])

        novo_chao = Chao(largurachao - 20)
        chao_chao.add(novo_chao)

    if is_off_tela(grupogaiola.sprites()[0]):
        grupogaiola.remove(grupogaiola.sprites()[0])
        grupogaiola.remove(grupogaiola.sprites()[0])

        gaiola = get_random_gaiola(900)
        grupogaiola.add(gaiola[0])
        grupogaiola.add(gaiola[1])
    
    grupopassaro.update()
    chao_chao.update()
    grupogaiola.update()

    grupopassaro.draw(tela)
    chao_chao.draw(tela)
    grupogaiola.draw(tela)

    pygame.display.update()

    if (pygame.sprite.groupcollide(grupopassaro, chao_chao, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(grupopassaro, grupogaiola, False, False, pygame.sprite.collide_mask)):
        break
