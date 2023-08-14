import pygame

window = pygame.display.set_mode((400, 700))
background = pygame.transform.scale(pygame.image.load('back.jpg'), (400, 700))
clock = pygame.time.Clock()


class Gamesprite(pygame.sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        pygame.sprite.Sprite.__init__(self)
        self.player_image = pygame.transform.scale(pygame.image.load(player_image), (width, height))
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def show(self):
        window.blit(self.player_image, (self.rect.x, self.rect.y))

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
sound = pygame.mixer.Sound("sound.mp3")
class Hero(Gamesprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] and self.rect.x < 300:
            self.rect.x += self.speed
        elif keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            sound.play()
        elif keys[pygame.K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed
        else:
            sound.stop()


player = Hero('ship2.png', 100, 100, 100, 100, 5)
class Enemy(Gamesprite):
    def update(self):
     self.rect.y += self.speed
     if self.rect.y > 700:
        self.rect.y = 0
height = 700
y = 0
y1 = -height
game = True
while game:
    window.blit(background, (0,0))
    player.show()
    player.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    y += 3
    window.blit(background, (0, y))
    y1 += 3
    window.blit(background, (0, y1))
    if y > height:
        y = -height
    if y1 > height:
        y1 = -height
    player.show()
    player.move()

    pygame.display.update()
    clock.tick(60)




