import pygame
import sys


from more_itertools.more import side_effect

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ninja Game')
        # Create a window
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img_pos = [160,250]
        self.movement = [False,False]


    def run(self):
        while True:
            self.screen.blit(self.img,self.img_pos)
            self.img_pos[1] += self.movement[1]
            self.screen.blit(self.img,(100,200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.KEYDOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.KEYDOWN:
                        self.movement[1] = False




            pygame.display.update()
            self.clock.tick(60)

Game().run()