import pygame, random

image_rock = pygame.image.load('sprites/stone.png')
sizes = [[64, 64], [96, 96], [128, 128], [160, 160], [198, 198]]
rocks = []

class Player(pygame.sprite.Sprite,):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:\Users\st3\Desktop\Olzhas\PythonPygame-main\sprites\spaceship.png')
        self.rect = self.image.get_rect()
        self.speed = 15
        

    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
           
        elif keys[pygame.K_s]:
            self.rect.y += self.speed
          
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed
          
        elif keys[pygame.K_d]:
            self.rect.x += self.speed
           

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        self.index = random.randint(0, 3)
        self.image = rocks[self.index]
        self.radius = sizes[self.index][0] // 2
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.rot_speed = random.randrange(-4, 4)
        self.rot_angle = 0
        self.dx = random.uniform(-7, 7)
        self.dy = random.uniform(1, 7)
        self.last_update = pygame.time.get_ticks()


    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            new_image = pygame.transform.rotate(rocks[self.index], self.rot_angle)
            self.rot_angle = (self.rot_angle + self.rot_speed) % 360
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        coords = self.rect.center
        #enemy bounces off the borders
        if(coords[0] + self.dx <- 128):
            self.kill()
        elif(coords[0] + self.dx > 928):
            self.kill()
        else:
            coords = coords[0] + self.dx, coords[1]
        if(coords[1] + self.dy <- 128):
            self.kill()
        elif(coords[1] + self.dy > 728):
            self.kill()
        else:
            coords = coords[0], coords[1] + self.dy
        self.rect.center = coords
        self.rotate()

