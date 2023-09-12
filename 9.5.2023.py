import pygame

pygame.display.set_caption("Olzhas game(shitty)")
RES = (1280, 720)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 25

running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
background = pygame.image.load("props.png")
sprites_left = (pygame.image.load("imp_left1.png"), pygame.image.load("imp_left2.png"), pygame.image.load("imp_left3.png"), pygame.image.load("imp_left4.png"))
sprites_right = (pygame.image.load("imp_right1.png"), pygame.image.load("imp_right2.png"), pygame.image.load("imp_right3.png"), pygame.image.load("imp_right4.png"))
sprites_idle = (pygame.image.load("imp_idle1.png"), pygame.image.load("imp_idle2.png"), pygame.image.load("imp_idle3.png"), pygame.image.load("imp_idle4.png"))


    


class Player(pygame.sprite.Sprite,):
    def __init__(self, left, right, idle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imp_idle1.png')
        self.rect = self.image.get_rect()
        self.speed = 25
        self.left = left
        self.right = right
        self.idle = idle
        self.c = 0
        self.XLR8tion = 12

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.rect.y += self.XLR8tion
            if self.c == len(self.idle) :
                self.c = 0
            self.image = self.idle[self.c]
            self.c += 1
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
            self.rect.y += self.XLR8tion
            if self.c == len(self.idle) :
                self.c = 0
            self.image = self.idle[self.c]
            self.c += 1
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.rect.x += self.XLR8tion
            if self.c == len(self.left) :
                self.c = 0
            self.image = self.left[self.c]
            self.c += 1
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
            self.rect.x += self.XLR8tion
            if self.c == len(self.right) :
                self.c = 0
            self.image = self.right[self.c]
            self.c += 1
        else:
            if self.c == len(self.idle) :
                self.c = 0
            self.image = self.idle[self.c]
            self.c += 1

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('portal.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def teleport(self, Player, tpcords):
        if Player.rect.x == self.rect.centerx and Player.rect.y == self.rect.centery:
            self.setCord(Player, tpcords)    

    def setCord(self, Player, tpcords):
        Player.rect.centerx = tpcords[0]
        Player.rect.centery = tpcords[1]
        





all_sprites = pygame.sprite.Group()
tps = pygame.sprite.Group()
p = Player(sprites_left, sprites_right, sprites_idle)
all_sprites.add(p)
t = Portal(700, 500)
t1 = Portal(500, 200)
tps.add(t)
tps.add(t1)

       

    
            
pygame.init()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    screen.fill(WHITE)
    t.teleport(p, (t1.rect.centerx, t1.rect.centery))
    #screen.blit(background, (0, 0))
    tps.draw(screen)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
    p.update()

pygame.quit()