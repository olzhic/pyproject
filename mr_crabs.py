import pygame

pygame.display.set_caption("Olzhas game(shitty)")
RES = (1280, 720)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 24

running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
background = pygame.image.load("props.png")
barrel_idle = (pygame.image.load("barrel1.png"), pygame.image.load("barrel2.png"), pygame.image.load("barrel3.png"))



    


class Player(pygame.sprite.Sprite,):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('mr_crab.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.speed = 15
        self.direct = ''



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direct = 'TOP'


        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direct = 'BOT'


        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direct = 'LEFT'

        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direct = 'RIGHT'
            

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, idle_anim):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('barrel1.png')
        self.image = pygame.transform.scale(self.image, (83, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.idle_anim = idle_anim
        self.c = 0

    def teleport(self, Player,):
        if Player.rect.colliderect(self.rect):
            if Player.direct == 'TOP' or Player.direct == 'LEFT':
                Player.rect.center = (Player.rect.centerx + 15, Player.rect.centery + 15)
            else:
                Player.rect.center = (Player.rect.centerx - 15, Player.rect.centery - 15)
        if self.c == len(self.idle_anim):
            self.c = 0
        self.image = self.idle_anim[self.c]
        self.c += 1

class Food(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:\\Users\\st3\\Desktop\\Olzhas\\dude.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def pick(self, Player):
        if Player.rect.colliderect(self.rect):
            self.image = None

    def draw(self):
        screen.blit(self.image, self.rect)
    
    


all_sprites = pygame.sprite.Group()
tps = pygame.sprite.Group()
pickups = pygame.sprite.Group()
p = Player()
t = Portal(200, 500, barrel_idle)
s = Food(900, 900)
pickups.add(s)
all_sprites.add(p)
tps.add(t)

       

    
            
pygame.init()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    screen.fill(WHITE)
    t.teleport(p)
    s.pick(p)
    s.draw()
    pickups.draw(screen)
    tps.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    p.update()

pygame.quit()