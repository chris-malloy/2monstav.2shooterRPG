import pygame
from math import hypot
from pygame.sprite import Sprite

class Dragon(Sprite):
    def __init__(self, screen):
        super(Dragon, self).__init__();
        self.x = 0
        self.y = 100
        self.screen = screen;
        self.image_original = pygame.image.load("./images/green_dragon.png")
        self.image = pygame.transform.scale(self.image_original,[150,150])
        self.flapping_index = 0
        # self.flapping_images = ['images/dragon2.png','images/dragon3.png']
    def fly(self):
        self.x += 10;
    def draw_me(self):
        self.screen.blit(self.image, [self.x, self.y])