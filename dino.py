import pygame

RES = (1280, 720)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 60

running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)



class cactus():
    def __init__(self, position):
        self.image = pygame.image.load("imp_left2.png")
        self.image = pygame.transform.scale(self.image, (100, 125))
        self.rect = self.image.get_rect()
        self.rect.center = position
        

    def kill(self):
        self.rect.x -= 10
        

    def draw(self):
        screen.blit(self.image, self.rect)
        if self.x < 0:
            self.kill


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

            


            
            
            
        
d = Dino((100, 500))
c = cactus((1000, 500))


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

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

