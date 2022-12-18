class Gaiola(pygame.sprite.Sprite):

    def __init__(self, inverted, xpos, ysize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('imagens/gaiola.png').convert_alpha()
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

        self.image = pygame.image.load('imagens/chãofinal.png').convert_alpha()
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