import random

class Claud:
    def __init__(self, pos, img, speed, depth):
        self.pos = list(pos)
        self.img = img
        self.speed = speed
        self.depth = depth

    def update(self):
        self.pos[0] += self.speed

    def render(self, surf, offset=(0,0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        surf.blit(self.img, (render_pos[0] % (surf.get_width() + self.img.get_width()) - self.img.get_width(), render_pos[1] % (surf.get_height() + self.img.get_height()) - self.img.get_height()))

class Clauds:
    def __init__(self, claud_images, count = 16):
        self.clauds = []

        for i in range(count):
            self.clauds.append(Claud((random.random() * 99999, random.random() * 99999), random.choice(claud_images),random.random() * 0.05 + 0.05, random.random() * 0.6 + 0.2))

        self.clauds.sort(key=lambda x: x.depth)

    def update(self):
        for claud in self.clauds:
            claud.update()

    def render(self, surf, offset=(0,0)):
        for claud in self.clauds:
            claud.render(surf, offset=offset)

