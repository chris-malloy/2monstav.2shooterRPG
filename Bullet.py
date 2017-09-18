import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,screen, the_player):
		super(Bullet,self).__init__();
		self.screen = screen;
		self.rect = pygame.Rect(0,0,5,20);
		self.color= (0,0,0);
		self.speed = 15;
		self.direction = 3;
		self.rect.centerx = the_player.x
		self.rect.top = the_player.y
		self.x = self.rect.x;
		self.y = self.rect.y;
		self.bullets = []
		self.explosion_index = 0
		self.explosion_image = 'images/explosion1.png'
		self.explosions = ['images/explosion2.png','images/explosion3.png','images/explosion4.png',
		'images/explosion5.png','images/explosion6.png','images/explosion7.png','images/explosion8.png','images/explosion9.png',
		'images/explosion10.png','images/explosion11.png','images/explosion12.png','images/explosion12.png','images/explosion13.png',
		'images/explsion14.png']
		self.tick = 0
	def update(self):
		if self.direction == 1: #up
			self.y -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		elif self.direction == 2: #right
			self.x += self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
		elif self.direction == 3: #down
			self.y += self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		else: #left
			self.x -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.x = self.x #update rect position
	def draw_bullet(self):
		if self.y > 600: 
			self.explosion()
		else:
			pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet!

	def explosion(self):
		self.tick += 1
		if self.tick % 10 == 0:
			if self.explosion_index == len(self.explosions) - 1:
				self.explosion_index = 0
			else:
				self.explosion_index += 1
				self.tick = 0
		self.screen.blit(pygame.image.load(self.explosions[self.explosion_index]), [self.x, 600])

