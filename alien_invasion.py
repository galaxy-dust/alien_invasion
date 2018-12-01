
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from Game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion 	v1.1")
	
	
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	play_button = Button(ai_settings, screen, "Play")
	
	while True:
		
		gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens, sb)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, bullets, aliens, ship, stats, sb)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
			
		gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, sb)

run_game()	
	
