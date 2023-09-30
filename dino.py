import pygame

RES = (1280, 720)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 60

running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)



class sky():
    def __init__(self,):
        self.image = pygame.image.load("sky.png")
        self.rect = self.image.get_rect()
    def draw(self):
        screen.blit(self.image, self.rect)
        


class Dino():
    def __init__(self, position):
        self.image = pygame.image.load("dino.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.y = 0
        self.step = 12
        self.max_jump = 25
        self.in_jump = False
        self.score = 0
        self.game_status = "Game"

    def jump(self):
        if self.in_jump:
            if self.y < self.max_jump:
                self.y += 1
                self.rect.y -= self.step
            elif self.y < self.max_jump * 2:
                self.y += 1
                self.rect.y += self.step    
            else:
                self.in_jump = False
                self.y = 0


    def draw(self):
        screen.blit(self.image, self.rect)





class cactus():
    def __init__(self, position,):
        self.image = pygame.image.load("imp_left2.png")
        self.image = pygame.transform.scale(self.image, (100, 125))
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.death = pygame.image.load("You_died.png")
        self.death = pygame.transform.scale(self.death, (500, 200))
        self.speed = 10

    def kill(self, Dino):
        self.rect.x -= self.speed
        if Dino.rect.colliderect(self.rect):
            screen.blit(self.death, (400, 200))
            self.rect.x += self.speed
        if  self.rect.x < -100:
            self.rect.x += 1400
        
        

    def draw(self):
        screen.blit(self.image, self.rect)
        if self.rect.x < 0:
            self.kill




d = Dino((100, 500))
c = cactus((1000, 500))
s = sky()
pygame.init() 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            d.in_jump = True

    

    screen.fill(WHITE)
    if d.game_status == "Game":
        d.jump()
        d.draw()
        c.draw()
        c.kill(d)
        s.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

