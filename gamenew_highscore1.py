# new game

import pygame
import random
from os import path
import os
import sys
from time import sleep

height = 480
width = 600
FPS = 60

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)

# initialize pygame and create window
pygame.init ()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ColorWow")
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
snd_dir = path.join(path.dirname(__file__),"snd")
score_file = path.join(path.dirname(__file__),"highest_score.txt")


font_name = pygame.font.match_font('Berlin Sans FB')
def draw_text(surf, text , size, x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)


def high_score(score):
    dir = path.dirname(__file__)
    with open(path.join(dir,"highest_score.txt"),'r') as f:
        try:
            highscore = int(f.read())
        except:
            highscore = 0
    if score>highscore:
        highscore=score
        with open(path.join(dir,"highest_score.txt"),'w') as f:
            f.write(str(highscore))

    draw_text(screen, "Highest score "+str(highscore),20,width/2,height-75)

class Button():
	def __init__(self, msg, x, y):
		self.width = 150
		self.height = 30
		self.font = pygame.font.Font(font_name, 24)
		self.text_color = BLACK
		self.bg_color = WHITE
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.prep_msg(msg,x,y)
		self.rect.centerx, self.rect.centery = x, y
		#self.rect.centerx, self.rect.centery = width/2, height/2
		screen.fill(self.bg_color, self.rect)
		screen.blit(self.msg_image, self.msg_image_rect)

	def prep_msg(self, msg, x, y):
		self.msg_image = self.font.render(msg, True, self.text_color, self.bg_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.centerx, self.msg_image_rect.centery = x, y


class Player(pygame.sprite.Sprite):
    def __init__(self, choice):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((50,50))
        #self.image.fill(GREEN)
        #switch(choice):
        if(choice == 1):
        	self.image = pygame.image.load(os.path.join(img_folder, "player4.jpeg")).convert()
        elif(choice == 2):
        	self.image = pygame.image.load(os.path.join(img_folder, "player5.jpg")).convert()
        elif(choice == 3):
        	self.image = pygame.image.load(os.path.join(img_folder, "player6.jpg")).convert()
        self.image = pygame.transform.scale(self.image, (45, 55))
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.bottom = height - 40
        self.speedx = 0
        self.speedy = 0

    def update(self):
       	self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
    	    self.speedx = -5
        if keystate[pygame.K_RIGHT]:
    	    self.speedx = 5
        if keystate[pygame.K_UP]:
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > width:
        	self.rect.right = width
        if self.rect.centerx == width:
        	self.rect.centerx = 0;
        if self.rect.left < 0:
    	    self.rect.left = 0
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
    #shoot_sound.play()

class Timer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((20,20))
    	#self.image.fill(WHITE)
        self.image = pygame.image.load(os.path.join(img_folder, "bullet5.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 10
        self.rect.bottom = height - 5
        self.speedx = 2

    def update(self):
        self.rect.x += self.speedx


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((40,40))
        #self.image.fill(RED)
        self.image = random.choice(right_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(-90,-50)
        self.speedy = random.randrange(1,8)
        #self.speedx = random.randrange(-3,3)

    def update(self):
    	#self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
    	    self.rect.x = random.randrange(0, width - self.rect.width)
    	    self.rect.y = random.randrange(-100, -50)
    	    self.speedy = random.randrange(1,8)

class Mob1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((40,40))
        #self.image.fill(BLUE)
        self.image = random.choice(wrong_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(-90,-50)
        self.speedy = random.randrange(1,8)
        #self.speedx = random.randrange(-3,3)

    def update(self):
    	#self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
    	    self.rect.x = random.randrange(0, width - self.rect.width)
    	    self.rect.y = random.randrange(-100, -50)
    	    self.speedy = random.randrange(1,8)

class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((40,40))
        self.image = random.choice(wrong_images)
	    #self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(-90,-50)
        self.speedy = random.randrange(1,8)
        #self.speedx = random.randrange(-3,3)

    def update(self):
    	#self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
    	    self.rect.x = random.randrange(0, width - self.rect.width)
    	    self.rect.y = random.randrange(-100, -50)
    	    self.speedy = random.randrange(1,8)

class Mob3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((40,40))
        #self.image.fill(ORANGE)
        self.image = random.choice(wrong_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(-90,-50)
        self.speedy = random.randrange(1,8)
        #self.speedx = random.randrange(-3,3)

    def update(self):
    	#self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
    	    self.rect.x = random.randrange(0, width - self.rect.width)
    	    self.rect.y = random.randrange(-100, -50)
    	    self.speedy = random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((10,10))
        #self.image.fill(WHITE)
        self.image = pygame.image.load(os.path.join(img_folder, "bullet8.png")).convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -40

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

def instructions():
	screen.fill(BLACK)
	draw_text(screen, "INSTRUCTIONS", 48, width/2, height/4)
	draw_text(screen, "Hit those alphabets, which are initials of name colour of that alphabet", 24, width/2, height/2)
	draw_text(screen, "Any type of collision leads to end of game.", 24, width/2, 3*height/5)
	button = Button("START GAME", width/2, 4*height/5)
	pygame.display.flip()
	waiting = True
	while waiting:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if button.rect.collidepoint(mouse_x, mouse_y):
					waiting = False

def show_go_screen():
    draw_text(screen, "True color", 64, width/2, height/4)
    draw_text(screen, "Arrows to move, Space to fire",24,width/2,height/2)
    button1 = Button('START GAME', width/4, 3*height/4)
    button2 = Button('INSTRUCTIONS', 3*width/4, 3*height/4)
    #draw_text(screen, "Press enter to begin",20,width/2,height*3/4)
    high_score(score)
    pygame.display.flip()
    waiting = True
    while waiting:
        #clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button1.rect.collidepoint(mouse_x, mouse_y):
                	waiting = False
                elif button2.rect.collidepoint(mouse_x, mouse_y):
                	waiting = False
                	instructions()                		
                	


def time_limit_exceeded(choice):
    screen.fill(BLACK)
    #draw_text(screen, "Game Over", 58, width/2, height/3)
    image = pygame.image.load(os.path.join(img_folder, "Nice-Game-Over.jpg")).convert()
    rect = image.get_rect()
    rect.centerx = width/2
    screen.blit(image, rect)
    draw_text(screen, "Sorry, You didn't score enough points", 30, width/2, height/2)
    #draw_text(screen, "Press ENTER to play again",20, width/2, 3*height/4)
    button1 = Button("START NEW GAME", width/4, 4*height/5)
    button2 = Button("CHANGE SHIP", width*3/4, 4*height/5)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
            	mouse_x, mouse_y = pygame.mouse.get_pos()
            	if button1.rect.collidepoint(mouse_x, mouse_y):
            		waiting = False
            		return choice
            	elif button2.rect.collidepoint(mouse_x, mouse_y):
            		waiting = False
            		choice = ship_selection()
            		return choice



def ship_hit(choice):
	screen.fill(BLACK)
	#draw_text(screen, "Game Over", 58, width/2, height/3)
	image = pygame.image.load(os.path.join(img_folder, "Nice-Game-Over.jpg")).convert()
	rect = image.get_rect()
	rect.centerx = width/2
	screen.blit(image, rect)
	draw_text(screen, "Your character is destroyed!!!!!", 30, width/2, height/2)
	#draw_text(screen, "Press ENTER to play again",20, width/2, 3*height/4)
	button1 = Button("START NEW GAME", width/4, 4*height/5)
	button2 = Button("CHANGE SHIP", width*3/4, 4*height/5)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if button1.rect.collidepoint(mouse_x, mouse_y):
					waiting = False
					return choice
				elif button2.rect.collidepoint(mouse_x, mouse_y):
					waiting = False
					choice = ship_selection()
					return choice


def mob_hit(choice):
	screen.fill(BLACK)
	#draw_text(screen, "Game Over", 58, width/2, height/3)
	image = pygame.image.load(os.path.join(img_folder, "Nice-Game-Over.jpg")).convert()
	rect = image.get_rect()
	rect.centerx = width/2
	screen.blit(image, rect)
	draw_text(screen, "Wrong charchter is hit!!!!", 30, width/2, height/2)
	#draw_text(screen, "Press ENTER to play again",20, width/2, 3*height/4)
	button1 = Button("START NEW GAME", width/4, 4*height/5)
	button2 = Button("CHANGE SHIP", width*3/4, 4*height/5)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if button1.rect.collidepoint(mouse_x, mouse_y):
					waiting = False
					return choice
				elif button2.rect.collidepoint(mouse_x, mouse_y):
					waiting = False
					choice = ship_selection()
					return choice

def ship_selection():
	screen.fill(BLACK)
	draw_text(screen, "Select your ship", 40, width/2, height/8)
	image1 = pygame.image.load(os.path.join(img_folder, "player4.jpeg")).convert()
	image1 = pygame.transform.scale(image1, (int(width/7),int(height/3)))
	rect1 = image1.get_rect()
	rect1.centerx = 3*width/14
	rect1.centery = 3*height/7
	image2 = pygame.image.load(os.path.join(img_folder, "player5.jpg")).convert()
	image2 = pygame.transform.scale(image2, (int(width/7),int(height/3)))
	rect2 = image2.get_rect()
	rect2.centerx = 7*width/14
	rect2.centery = 3*height/7
	image3 = pygame.image.load(os.path.join(img_folder, "player6.jpg")).convert()
	image3 = pygame.transform.scale(image3, (int(width/7),int(height/3)))
	rect3 = image1.get_rect()
	rect3.centerx = 11*width/14
	rect3.centery = 3*height/7
	screen.blit(image1, rect1)
	screen.blit(image2, rect2)
	screen.blit(image3, rect3)
	draw_text(screen, "Select your aircraft", 30, width/2, 4*height/5)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x,mouse_y = pygame.mouse.get_pos()
				if rect1.collidepoint(mouse_x, mouse_y):
					waiting = False
					sel=1	
					return sel;
				elif rect2.collidepoint(mouse_x, mouse_y):
					waiting = False
					sel=2	
					return sel;
				elif rect3.collidepoint(mouse_x, mouse_y):
					waiting = False
					sel=3
					return sel;


wrong_images = []

wrong_list = [
                "b1.png",'b2.png','b3.png','b4.png','b5.png','b7.png','b8.png','b9.png','b12.png',
	        'b13.png','g1.png','g2.png','g3.png','g4.png','g5.png','g6.png','g8.png',
                'g9.png','o2.png','o3.png','o4.png','o5.png','o6.png','o7.png','o8.png','o9.png','o10.png',
                'p1.png','p2.png','p3.png','p4.png','p5.png','p6.png','p7.png','p9.png','p10.png','p12.png',
                'r2.png','r3.png','r4.png','r5.png','r6.png','r7.png','r8.png','r9.png','r10.png','r11.png','r12.png',
		'y1.png','y2.png','y4.png','y5.png','y6.png','y7.png','y8.png','y9.png'
             ]

right_images = []

right_list = [ 'b6.png','b14.png','b15.png','g7.png','o1.png','p8.png','p11.png','r1.png','y3.png' ]

col_list = [ 40, 120, 200, 280, 360 ]

timer_images = []

timer_list = ['timer1.png','timer2.png','timer3.png','timer4.png']


for img in timer_list:
     	timer_images.append(pygame.image.load(path.join(img_folder, img)).convert())

for img in wrong_list:
     	wrong_images.append(pygame.image.load(path.join(img_folder, img)).convert())

for img in right_list:
     	right_images.append(pygame.image.load(path.join(img_folder, img)).convert())


shoot_sound = pygame.mixer.Sound(path.join(snd_dir,"laser3.wav"))
pygame.mixer.music.load(path.join(snd_dir,'Hypnotic Puzzle.wav'))
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)#loops=(-1)


# Game loop
game_over = True
running = True
score = 0

count = 1  #To make sure that welcome and plane selection window appears only once

while running:
    if game_over:
    	if(count>0):
    		show_go_screen()
    		choice = ship_selection()
    		ship_selection()
    		count=0
    	game_over = False
    	all_sprites = pygame.sprite.Group()
    	mobs = pygame.sprite.Group()
    	enemy = pygame.sprite.Group()
    	bullets = pygame.sprite.Group()
    	player = Player(choice)
    	all_sprites.add(player)
    	time = Timer()
    	all_sprites.add(time)
    	for i in range(1):
    		m = Mob()
    		n = Mob1()
    		o = Mob2()
    		p = Mob3()
    		all_sprites.add(m)
    		all_sprites.add(n)
    		all_sprites.add(o)
    		all_sprites.add(p)
    		mobs.add(n)
    		mobs.add(o)
    		mobs.add(p)
    		enemy.add(m)
    	score = 0
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
    	# check for closing window
    	if event.type == pygame.QUIT:
    		running = False
    	elif event.type == pygame.KEYDOWN:
    		if event.key == pygame.K_SPACE:
    			player.shoot()

   	#update
    all_sprites.update()

    # check if bullet hits mob
    hits = pygame.sprite.groupcollide(bullets , enemy ,True ,True)
    for hit in hits:
        score += 1
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
        enemy.add(m)
        time.kill()
        time = Timer()
        #all_sprites.remove(time)
        all_sprites.add(time)
        #time.update.rect.x = 0

    # check if bullet hits other than enemy
    hits = pygame.sprite.groupcollide(bullets , mobs ,True ,True)
    if hits:
        game_over = True
        sleep(0.5)
        choice = mob_hit(choice)


    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, False) or pygame.sprite.spritecollide(player, enemy, False)
    if hits:
        game_over = True
        sleep(0.5)
        choice = ship_hit(choice)

    if time.rect.right > width:
        game_over = True
        choice = time_limit_exceeded(choice)


    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen , str(score), 22, width/2, 10)

    # *after* drawing everything, flip the display
    pygame.display.flip()
    screen.fill(BLACK)

pygame.quit()