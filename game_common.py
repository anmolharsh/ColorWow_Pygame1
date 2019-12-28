import pygame
from gamenew_highscore1 import run_game,draw_text,Button
from gamenew_server import run_server
from gamenew_client import run_client	
import random
from os import path
import os
import sys
from time import sleep

HOST = '127.0.0.1'
PORT = 23456
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
explosion = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_folder, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (60, 60))
    explosion.append(img)

font_name = pygame.font.match_font('Berlin Sans FB')

def multi():
	screen.fill(BLACK)
	draw_text(screen, "True Color", 100, width/2, height/4)
	draw_text(screen, "You want to play as:", 64, width/2, height/2)
	button1 = Button("SERVER", width/4, 4*height/5)
	button2 = Button("CLIENT", width*3/4, 4*height/5)
	draw_text(screen, "OR", 24, width/2, 4*height/5)
	pygame.display.flip()
	waiting = True
	while waiting:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if button1.rect.collidepoint(mouse_x, mouse_y):
					run_server()
					waiting = False
				elif button2.rect.collidepoint(mouse_x, mouse_y):
					run_client()
					waiting = False

def instructions():
	screen.fill(BLACK)
	draw_text(screen, "INSTRUCTIONS", 48, width/2, height/4)
	draw_text(screen, "Hit those alphabets, which are initials of name colour of that alphabet", 24, width/2, height/2)
	draw_text(screen, "Any type of collision leads to end of game.", 24, width/2, 3*height/5)
	button = Button("MAIN MENU", width/2, 4*height/5)
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
					start_screen()

def start_screen():
	screen.fill(BLACK)
	draw_text(screen, 'True Color', 128, width/2, height/5)
	button1 = Button("SINGLE PLAYER", width/2, 3*height/5-60)
	button2 = Button("MULTI PLAYER", width/2, 3*height/5)
	button3 = Button("INSTRUCTIONS", width/2, 3*height/5+60)
	pygame.display.flip()
	waiting = True
	while waiting:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if button1.rect.collidepoint(mouse_x, mouse_y):
					waiting = False
					run_game()
				elif button2.rect.collidepoint(mouse_x, mouse_y):
					waiting = False
					multi()
				elif button3.rect.collidepoint(mouse_x, mouse_y):
					waiting = False
					instructions()




start_screen()


pygame.quit()