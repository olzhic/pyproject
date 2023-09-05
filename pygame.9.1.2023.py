import pygame

RES = (1280, 720)

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
FPS = 60

running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Block():
    def __init__(self, x, y, height, width,):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 10

    def update(self, sc):
        self.x += self.speed
        if self.x > 1230 or self.x < 0:
            self.speed =- self.speed
        pygame.draw.rect(sc, WHITE, pygame.Rect(self.x, self.y, self.width, self.height))
            
            
            
        
            

b = Block(50, 50, 50, 50)
pygame.init()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    screen.fill(RED)
    b.update(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

