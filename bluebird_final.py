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

pontos = int(0)

pontos += int(1)
gaiola_gap = 160

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Blue Bird')

fundo = pygame.image.load('images/fundo_jogo.png')
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
fundo_game_over = pygame.image.load('images/fundo_game_over.png')

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
        self.rect[0] -= velocidade_do_jogo

class Chao(pygame.sprite.Sprite):

    def __init__(self, ichao):
        pygame.sprite.Sprite. __init__(self)

        self.image = pygame.image.load('images/chao_final.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(largura_chao, altura_chao))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = ichao
        self.rect[1] = altura_tela - altura_chao

    def update(self):
        self.rect[0] -= velocidade_do_jogo

class Game:

    def __init__(self):
        #tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((largura_tela, altura_tela))
        pygame.display.set_caption('Blue Bird')
        self.clock = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(FONTE)
        
    def novo_jogo(self):
        #classes das sprites do jogo
        global pontos
        global mensagem
        
        self.todas_as_sprites = pygame.sprite.Group()
        grupopassaro = pygame.sprite.Group()
        passaro = Passaro()
        grupopassaro.add(passaro)
        pontos = int(0)

        grupo_chao = pygame.sprite.Group()
        for i in range(2):
            chao = Chao(largura_chao * i)
            grupo_chao.add(chao)

        grupogaiola = pygame.sprite.Group()
        for i in range(2):
            gaiola = get_random_gaiola(largura_tela * i + 800)
            grupogaiola.add(gaiola[0])
            grupogaiola.add(gaiola[1])

        self.jogando = True
        while self.jogando:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    if self.jogando:
                        self.jogando = False
                    self.esta_rodando = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pygame.mixer.Sound('audios/sfx_wing.wav').play()
                        passaro.pulo()
        
            self.tela.blit(fundo, (0, 0))

            if is_off_tela(grupo_chao.sprites()[0]):
                grupo_chao.remove(grupo_chao.sprites()[0])

                novo_chao = Chao(largura_chao - 20)
                grupo_chao.add(novo_chao)

            if is_off_tela(grupogaiola.sprites()[0]):
                grupogaiola.remove(grupogaiola.sprites()[0])
                grupogaiola.remove(grupogaiola.sprites()[0])

                gaiola = get_random_gaiola(900)
                grupogaiola.add(gaiola[0])
                grupogaiola.add(gaiola[1])

            grupopassaro.draw(tela)
            grupo_chao.draw(tela)
            grupogaiola.draw(tela) #desenhando as sprites
            
            grupopassaro.update()
            grupo_chao.update()
            grupogaiola.update() #atualizando as sprites

            if (pygame.sprite.groupcollide(grupopassaro, grupo_chao, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(grupopassaro, grupogaiola, False, False, pygame.sprite.collide_mask)):
                self.mostrar_tela_game_over()
            else:
                pontos = pontos + 1
                mensagem = '{:02d}'.format(pontos)
                exibe_mensagem(mensagem, 40, BRANCO, largura_tela / 2, 30)
            
            pygame.display.flip()

    def mostrar_texto(self, texto, tamanho, cor, x, y):
        #Exibe um texto na tela do jogo
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (x, y)
        self.tela.blit(texto, texto_rect)

    def mostrar_start_logo(self, x, y):
        self.backgroung_1 = pygame.image.load('images/fundo_inicio.png')
        start_logo_rect = self.backgroung_1.get_rect()
        start_logo_rect.midtop = (x, y)
        self.tela.blit(self.backgroung_1, start_logo_rect)

    def mostrar_tela_start(self):
        pygame.mixer.music.load('audios/bird_3.wav')
        pygame.mixer.music.play()

        self.mostrar_start_logo(largura_tela / 2, 0)

        self.mostrar_texto('Pressione uma tecla para jogar', 28, BRANCO, largura_tela / 2, 300)

        pygame.display.update()
        self.esperar_por_jogador()
    
    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == KEYUP:
                    esperando = False    
                    pygame.mixer.music.stop()         
                    pygame.mixer.Sound('audios/sfx_wing.wav').play()

    def mostrar_tela_game_over(self):
        tela.fill(PRETO)
        tela.blit(fundo_game_over, (0,0))
        exibe_mensagem('GAME OVER', 100, BRANCO, largura_tela / 2, 120)
        exibe_mensagem('Sua pontuação é de: ' + str(mensagem), 26, BRANCO, largura_tela / 2, 250)
        exibe_mensagem(f'Aperte ESPAÇO para jogar de novo', 26, BRANCO, largura_tela / 2, 290)

        pygame.display.update()
        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pygame.mixer.Sound('audios/sfx_wing.wav').play()
                        self.novo_jogo()
        
g = Game()
g.mostrar_tela_start()

while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()