import pygame # We have access to pygame because we sintalled it in  $ pip install pygame
import time
from pygame.sprite import Group, groupcollide; 
from Player import Player #custom classes here
from Bad_guy import Bad_Guy; 
from Bullet import Bullet
from Latios import Latios
from Dragon import Dragon
import random

pygame.init();

pygame.mixer.init()
pygame.mixer.music.load("sounds/music.wav")
pygame.mixer.music.play()

explosion_sound = pygame.mixer.Sound("sounds/8-BIt-SFX_Explosion_01.wav")

pygame.font.init()

screenx = 1000;
screeny = 800;
screen_size =(screenx, screeny);
# black = (170, 238, 187)

background_image_one = pygame.image.load("./images/space.jpg")
background_image_one_resized = pygame.transform.scale(background_image_one, screen_size)
background_image_two = pygame.image.load("./images/background3.png");
background_image_two_resized = pygame.transform.scale(background_image_two, screen_size)

screen = pygame.display.set_mode(screen_size);
pygame.display.set_caption("Hi");

the_player = Player("./images/ff1.tiff", 100, 500, screen) # dont need the image, the x or the y
bad_guy = Bad_Guy(screen, 700, 575);
latios = Latios(screen);
dragon = Dragon(screen)
bullets = Group(); #make a new group called bullets, it's a pygame "list";
hero_group = Group();
enemy_group = Group();

hero_group.add(the_player);
enemy_group.add(bad_guy);


def message1_display(text): #display what kind of text you want
	largeText = pygame.font.Font(None ,90)
	start_text = largeText.render(text, True, (205, 224, 255));
	screen.blit(start_text, [100, 100]);
	pygame.display.update()

def message2_display(text):
	largeText = pygame.font.Font(None ,70)
	story = largeText.render(text, True, (205, 224, 255));
	# start_text = largeText.render(text, True, (205, 224, 255));
	screen.blit(story, [230,300]);
	# screen.blit(start_text, [screenx/2 -125, screeny/2]);
	pygame.display.update()

def message3_display(text):
	largeText = pygame.font.Font(None,70)
	prompt = largeText.render(prompt, True, (205, 224, 255))
	screen.blit(prompt, [screenx/2 - 150, screeny/2])
	pygame.display.update()

def check_collision():
	pygame.sprite.groupcollide(hero_group, enemy_group, False, True);
	pygame.sprite.groupcollide(hero_group, bullets, False, False)
		
def health():
	text = pygame.font.Font(None, 20);
	healt_c = text.render("HEALTH_COUNT: %d" % the_player.health, True, (0, 0, 0))
	monster_killed = text.render("Monster Killed: %d" %bad_guy.bad_guy_count, True, (0, 0, 0));
	screen.blit(healt_c, [100, 50])
	screen.blit(monster_killed, [100, 70])


def game_loop():
	starting_text = True;
	game_on = True;
	tick = 0;
	last_bullet_drop = time.time()
	while game_on: #will run forever until break
		tick+=1; #keeps track of seconds/frames per second
		for event in pygame.event.get(): #loop through all the pygame events, gave it a escape patch
			if event.type == pygame.QUIT:
				game_on = False;
			elif(event.type ==pygame.KEYDOWN): 
				# if(event.key == 273):
				# 	the_player.should_move("up", True);
				# elif(event.key == 274):
				# 	the_player.should_move("down", True);
				if(event.key == pygame.K_d):
					the_player.should_move("right", True);
				elif(event.key == pygame.K_a):
					the_player.should_move("left", True);
					the_player.transform_image();
				elif(event.key == 32):
					the_player.swinging = True;
				elif(event.key == pygame.K_RSHIFT):
					the_player.jump(True);
			elif(event.type ==pygame.KEYUP): 
				#if(event.key == 273):	
				# 	the_player.should_move("up", False);
				# elif(event.key == 274):
				# 	the_player.should_move("down", False);  
				if(event.key == pygame.K_d):	
					the_player.should_move("right", False);
				elif(event.key == pygame.K_a):
					the_player.should_move("left", False);
					the_player.transform_image();
				elif(event.key == 32):
					the_player.swinging = False ;
				elif(event.key == pygame.K_RSHIFT):
					the_player.jump(False);

		screen.blit(background_image_one_resized, [0,0])
		if(starting_text == True): #added welcome player logo at the start of the game.
			message1_display("Welcome Brave Adventurer");
			message2_display("Are you ready to play?")
			
			if(tick % 100 == 0):	
				starting_text = False;
		else:
			screen.blit(background_image_two_resized, [0,0])
			for i in enemy_group: #this moves the bad_guy in the enemy group towards the hero
				i.update_me(the_player)
			if(len(enemy_group)== 0): #checks to see if anyone is in the enemy group
				bad_guy.bad_guy_count+=1;
				bad_guy_new = Bad_Guy(screen, 700, 575) #if there isnt, make a new bad guy
				bad_guy_new.draw_me(); #draw him
				enemy_group.add(bad_guy_new); #add him to the bad guy group
			else:
				for bad in enemy_group: #checks the enemy group, for anyhting
					bad.draw_me(); #if there is, draw something, if not don't draw.
			
			new_bullet = Bullet(screen, latios);
			new_bullet1 = Bullet(screen, dragon)
			if(time.time() > last_bullet_drop + 2):
				bullets.add(new_bullet);
				bullets.add(new_bullet1)
				last_bullet_drop = time.time()

			the_player.update()
			the_player.draw_me();
			check_collision();
			health();
			if(dragon.x > 1000):
				dragon.x = 0
			else:
				dragon.fly();
				dragon.draw_me();
			if(latios.x < 0):
				latios.x = 900;
			else:
				latios.fly();
				latios.draw_me();
		for bullet in bullets:
			bullet.update()
			bullet.draw_bullet();
			if bullet.y > 600:
				explosion_sound.play()

		pygame.display.flip();
game_loop();



#TODO: slow done hero swing
#TODO: create lose screen and ask player if they want to play again
#TODO: ask user if they want to play
#TODO: make collision between hero pixels correct
#TODO: check the image for flipping