import pygame


class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)

    def anim(self, image, tick, frames):
        self.tick += 1

        if self.tick == tick:
            self.tick = 0
            self.frame += 1

        if self.frame == frames:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/" + image + str(self.frame) + ".png")

class Bee(Obj):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")
        self.sound_block = pygame.mixer.Sound("assets/sounds/bateu.ogg")


        self.lives = 3
        self.pts = 0

    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    def collision(self, group, name):

        name = name
        collision = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == "Flower" and collision:
            self.pts += 1
            self.sound_pts.play()
        elif name == "Spider" and collision:
            self.lives -= 1
            self.sound_block.play()

class Text:

    def __init__(self, size, text):

        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, True, (255,255,255))

    def drawing(self, window, x, y):
        window.blit(self.render, (x,y))

    def update_text(self, update):
        self.render = self.font.render(update, True, (255, 255, 255))

