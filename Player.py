import pygame
from pygame.sprite import Sprite

class Player(Sprite):
	def __init__(self, image,start_x, start_y, screen):
		super(Player,self).__init__(); #because it's a subclass, you have to call the parent class Sprite
		self.image_original = pygame.image.load(image);
		self.image = pygame.transform.scale(self.image_original, [170, 170])
		self.x = start_x;
		self.y = start_y;
		self.health = 3;
		self.rect = pygame.Rect(start_x, start_y, 100, 100) #added myself
		self.speed = 20;
		self.screen = screen;
		self.should_move_up = False;
		self.should_move_down = False;
		self.should_move_left = False;
		self.should_move_right = False;
		self.image_group = [];
		self.index = 0;
		self.image_group.append(self.image);
		self.image_original_2 = pygame.image.load("./images/ff2.tiff")
		self.image_original_2_transform = pygame.transform.scale(self.image_original_2, [170,170])
		self.image_group.append(self.image_original_2_transform);
		self.image_original_3 = pygame.image.load("./images/ff3.tiff")
		self.image_original_3_transform = pygame.transform.scale(self.image_original_3, [170,170])
		self.image_group.append(self.image_original_3_transform)
		self.image_original_4 = pygame.image.load("./images/ff4.tiff")
		self.image_original_4_transform = pygame.transform.scale(self.image_original_4, [170,170])
		self.image_group.append(self.image_original_4_transform)
		self.image_original_5 = pygame.image.load("./images/ff5.tiff")
		self.image_original_5_transform = pygame.transform.scale(self.image_original_5, [170,170])
		self.image_group.append(self.image_original_5_transform);
		self.swinging = False;


	def draw_me(self):
		if(self.should_move_up):
			self.y -= self.speed;
		elif(self.should_move_down):
			self.y += self.speed;
		if(self.should_move_left):
			self.x -= self.speed;
		elif(self.should_move_right):
			self.x += self.speed;
		self.rect = pygame.Rect(self.x, self.y, 100, 100)
		self.screen.blit(self.image, [self.x, self.y]);

	def should_move(self, direction, yes_or_no):
		if(direction =="up"):
			self.should_move_up = yes_or_no; #the key is down, update itself;
		if(direction =="down"):
			self.should_move_down = yes_or_no;
		if(direction =="left"):
			self.should_move_left = yes_or_no;
		if(direction =="right"):
			self.should_move_right = yes_or_no;
			
	def transform_image(self):
		if self.should_move_right == True:
			self.image = self.image
			self.screen.blit(self.image, [self.x, self.y])
		elif self.should_move_left == True:
			self.image = pygame.transform.flip(self.image, True, False);
			self.screen.blit(self.image, [self.x, self.y])


	def update(self):
		if(self.swinging or self.index > 0):
			self.index +=1;
			if(self.index >= len(self.image_group)):
				self.index = 0;
			self.image = self.image_group[self.index]
			self.screen.blit(self.image, [self.x, self.y])

	def jump(self, true_or_false):
		if(true_or_false == True):
			self.y -=110;
			self.screen.blit(self.image, [self.x, self.y])
		else:
			self.y +=110;
			self.screen.blit(self.image, [self.x, self.y])