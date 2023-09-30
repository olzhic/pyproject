import pygame
import random

RES = (400, 600)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 60

running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
transparent = (0, 0, 0, 0)

        

class level(pygame.sprite.Sprite,):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("road.png")
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self):
        screen.blit(self.image)


class Car(pygame.sprite.Sprite,):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("player_car.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.y = 0
        self.speed = 12
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed
        
    def draw(self):
        screen.blit(self.image, self.rect)

class enemy_car(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load("enemycar.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 300), 0)
        self.death = pygame.image.load("You_died.png")
        self.death = pygame.transform.scale(self.death, (500, 200))
        self.speed = 10
        

    def update(self):
        self.rect.y += self.speed
        if  self.rect.y > 700:
            self.rect.y = -100
            self.rect.center = (random.randint(50, 300), -100)

    def kill(self, Car):
        if Car.rect.colliderect(self.rect):
            screen.blit(self.death, (100, 100))
            self.rect.y -= self.speed
        
        
        

    def draw(self):
        screen.blit(self.image, self.rect)
        if self.rect.x < 0:
            self.kill


class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, 300), random.randint(50, 300))
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.speed = 10

    def draw(self):
        screen.blit(self.image, self.rect)
        

    def collect(self, Car):
        self.rect.y += self.speed
        if  self.rect.y > 700:
            self.rect.y = -100
            self.rect.center = (random.randint(50, 300), -100)
        if Car.rect.colliderect(self.rect):
            self.kill()

all_sprites = pygame.sprite.Group()
d = Car((100, 500))
c = enemy_car()
cn = coin()
l = level((200,300))
all_sprites.add(l)
all_sprites.add(d)
all_sprites.add(c)
all_sprites.add(cn)


pygame.init() 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill(WHITE)

    
    all_sprites.draw(screen)
    
    all_sprites.update()
    cn.collect(d)
    c.kill(d)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()