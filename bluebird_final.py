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

        def novo_jogo(self):
        #classes das sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        grupopassaro = pygame.sprite.Group()
        passaro = Passaro()
        grupopassaro.add(passaro)

        grupo_chao = pygame.sprite.Group()
        for i in range(2):
            chao = Chao(largura_chao * i)
            grupo_chao.add(chao)

        grupogaiola = pygame.sprite.Group()
        for i in range(2):
            gaiola = get_random_gaiola(largura_tela * i + 800)
            grupogaiola.add(gaiola[0])
            grupogaiola.add(gaiola[1])

        while True:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    if self.jogando:
                        self.jogando = False
                    self.esta_rodando = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
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
            
            pygame.display.flip()

            if (pygame.sprite.groupcollide(grupopassaro, grupo_chao, False, False, pygame.sprite.collide_mask) or pygame.sprite.groupcollide(grupopassaro, grupogaiola, False, False, pygame.sprite.collide_mask)):
                break