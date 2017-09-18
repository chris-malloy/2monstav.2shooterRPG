import pygame
from math import hypot
from pygame.sprite import Sprite

class Bad_Guy(Sprite):
	def __init__(self, screen, x ,y ):
		super(Bad_Guy, self).__init__();
		self.image_original = pygame.image.load("./images/monster1.tiff")
		self.image = pygame.transform.scale(self.image_original, [100, 100])
		self.image_group = []
		self.image_group.append(self.image);
		self.image_original2 = pygame.image.load("./images/monster2.tiff")
		self.image_original2_transform = pygame.transform.scale(self.image_original2, [100, 100])
		self.image_group.append(self.image_original2_transform);
		self.index = 0;
		self.x = x;
		self.y = y;
		self.bad_guy_count = 0;
		self.rect = pygame.Rect(x,y,100,100) #added
		self.screen = screen;
		self.speed = 4;
	def update_me(self, the_player):
		# dx = self.x - the_player.x
		# dy = self.y - the_player.y
		# dist = hypot(dx,dy)
		# dx = dx / dist
		# dy = dy / dist
		# self.x -= dx * self.speed
		# self.y -= dy * self.speed
		self.x -= self.speed;
	def draw_me(self):
		# self.rect.left = self.x
		# self.rect.top = self.y
		self.index +=1;
		if(self.index >= len(self.image_group)):
			self.index = 0;
		self.image = self.image_group[self.index]
		self.rect = pygame.Rect(self.x,self.y,100,100)
		self.screen.blit(self.image, [self.x, self.y])
