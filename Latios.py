import pygame
from math import hypot
from pygame.sprite import Sprite

class Latios(Sprite):
    def __init__(self, screen):
        super(Latios, self).__init__();
        self.x = 900
        self.y = 200
        self.screen = screen;
        self.image = pygame.image.load("./images/latios.png")
        self.flapping_index = 0
        # self.flapping_images = ['images/dragon2.png','images/dragon3.png']
    def fly(self):
        self.x -= 10;
    def draw_me(self):
        self.screen.blit(self.image, [self.x, self.y])