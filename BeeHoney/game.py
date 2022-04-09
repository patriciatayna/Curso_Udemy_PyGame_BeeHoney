from obj import Obj, Bee, Text
import random

class Game:

    def __init__(self):

        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)

        self.spider = Obj("assets/spider1.png", random.randrange(0, 300), -50)
        self.flower = Obj("assets/flower1.png", random.randrange(0,300), -50)
        self.bee = Bee("assets/bee1.png", 150, 600)

        self.score = Text(120, "0")
        self.lives = Text(60, "3")

        self.change_scene = False

    def draw(self, window):
        self.bg.drawing(window)
        self.bg2.drawing(window)

        self.bee.drawing(window)

        self.spider.drawing(window)
        self.flower.drawing(window)

        self.score.drawing(window, 160, 50)
        self.lives.drawing(window, 50, 50)

    def update(self):
        self.move_bg()

        self.spider.anim("spider", 8, 5)
        self.flower.anim("flower", 8, 3)
        self.bee.anim("bee", 1, 5)

        self.move_spiders()
        self.move_flowers()

        self.bee.collision(self.spider.group, "Spider")
        self.bee.collision(self.flower.group, "Flower")

        self.score.update_text(str(self.bee.pts))
        self.lives.update_text(str(self.bee.lives))

        self.gameover()

    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_spiders(self):
        self.spider.sprite.rect[1] += 10

        if self.spider.sprite.rect[1] >= 700:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png", random.randrange(0, 290), -50)

    def move_flowers(self):
        self.flower.sprite.rect[1] += 6

        if self.flower.sprite.rect[1] >= 700:
            self.flower.sprite.kill()
            self.flower = Obj("assets/flower1.png", random.randrange(0, 290), -50)

    def gameover(self):
        if self.bee.lives <= 0:
            self.change_scene = True

