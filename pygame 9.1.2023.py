import pygame
import random
class mySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("caco.png")
        self.rect = self.image.get_rect()
##        slef.rect(50,50,self.image.get_width(), self.image.get_height())

    def update(self,x,y):
        self.rect.x = x
        self.rect.y = y

class newSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect()

    def update(self,x,y):
        self.rect.x = x
        self.rect.y = y

class otherSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("caco.png")
        self.rect = self.image.get_rect()

    def update(self,x,y):
        self.rect.x = x
        self.rect.y = y

def main():
    """ Set up the game and run the main game loop """
    pygame.init() # prepare the pygame module for use
    surfaceSz = 480 # Desired physical surface size, in pixels.
    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surfaceSz, surfaceSz))

    small_rect = (300, 200, 150, 90)
    some_color = (255,0,0)
    main_surface.fill((0,200,255))

    s = mySprite()
    all_sprites = pygame.sprite.Group()

    s.add(all_sprites)

    delta_x = 5
    delta_y = 5
    u = 1 # x coord
    v = 1 # y coord

    clock = pygame.time.Clock()
    while True:
        ev = pygame.event.poll() # look for any event
        if ev.type == pygame.QUIT: # window close button clicked?
            break # ... leave game loop

        main_surface.fill((0,200,255))

        #u += delta
        #if u >= 440:
        #    delta = -5
        #elif u < 0:
        #    delta = 5

        u += delta_x
        v += delta_y
        if (v >=440): #assuming your y axis is 440 pixels
            delta_y = -5
        elif v<=0 :
            delta_y = 5

        if u >= 440: #440 pixels u have
            delta = -5
        elif u < 0:
            delta = 5 #Go up by 5


        all_sprites.update(u,50)
        pos =(random.randint(0, surfaceSz), random.randint(0, surfaceSz))
        all_sprites.draw(main_surface)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        clock.tick(60)

    pygame.quit() # once we leave the loop, close the window.

main()