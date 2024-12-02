import pygame

import sys

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntiti
from scripts.tilemap import Tilemap


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Ninja Game')
        # Create a window
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320,240))

        self.clock = pygame.time.Clock()

        # Add an image
        # self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        # self.img.set_colorkey((0,0,0))

        # movement
        # self.img_pos = [160,250]
        self.movement = [False,False]

        # Collision Section
        # self.collision_area = pygame.Rect(50,50,300,50)

        self.assets = {
            'decor'      : load_images('tiles/decor'),
            'grass'      : load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone'      : load_images('tiles/stone'),
            'player'     : load_image('entities/player.png')
        }

        # print(self.assets)

        self.player = PhysicsEntiti(self, 'player', (50,50),(8,15))
        self.tilemap = Tilemap(self, tile_size=16)


    def run(self):
        while True:
            # Movement section

            self.display.fill((14,219,248))

            self.tilemap.render(self.display)

            self.player.update(self.tilemap,(self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            # print(self.tilemap.tiles_around(self.player.pos))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False



            self.screen.blit(pygame.transform.scale(self.display,self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

Game().run()