
import pygame

import sys
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()
			
def check_keyup_events(event, ship):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets, stats, play_button, aliens ,sb):

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, screen, aliens, ship, stats, bullets, play_button, mouse_x, mouse_y, sb)
			
def check_play_button(ai_settings, screen, aliens, ship, stats, bullets, play_button, mouse_x, mouse_y, sb):
	buttom_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if buttom_clicked and not stats.game_active:
	
		ai_settings.initialize_dynamic_settings()
		
		
		pygame.mouse.set_visible(False)
		
		
		stats.reset_stats()
		stats.game_active = True
		sb.prep_score()
		sb.prep_highest_score()
		sb.prep_level()
		sb.prep_ships()
	
		
		aliens.empty()
		bullets.empty()
		
		
		create_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()
	
def fire_bullet(ai_settings, screen, ship, bullets):
	
	if len(bullets)< ai_settings.bullet_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)

def update_bullets(ai_settings, screen, bullets, aliens, ship, stats, sb):
	
	
	bullets.update()
	
	
	for bullet in bullets.copy():
		if bullet.rect.bottom <=0:
			bullets.remove(bullet)
	
	
	check_bullet_alien_collisions(ai_settings, screen, aliens, ship, bullets, stats, sb)

def check_bullet_alien_collisions(ai_settings, screen, aliens, ship, bullets, stats, sb):
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for aliens in collisions.values():
			stats.score += (ai_settings.alien_point * len(aliens))
		sb.prep_score()
		check_highest_score(stats, sb)
	if len(aliens) == 0:
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings, screen, aliens, ship)
		
		stats.level += 1
		sb.prep_level()

def check_highest_score(stats, sb):
	if stats.score > stats.highest_score:
		stats.highest_score = stats.score
		sb.prep_highest_score()
			
def get_number_alien_x(ai_settings, alien_width):
	
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_alien_x = int(available_space_x / (2 * alien_width))
	return 	number_alien_x

def get_number_alien_y(ai_settings, alien_height, ship_height):
	
	available_space_y = ai_settings.screen_height - ship_height - 3 * alien_height
	number_alien_y = int(available_space_y / (2 * alien_height))
	return number_alien_y

def create_alien(ai_settings, screen, aliens, alien_number, alien_row):
	
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = 1.5 * alien.rect.height + 1.5 * alien.rect.height * alien_row
	aliens.add(alien)
	
def create_fleet(ai_settings, screen, aliens, ship):
	
	
	alien = Alien(ai_settings, screen)
	number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
	number_rows = get_number_alien_y(ai_settings, alien.rect.height, ship.rect.height)
	
	
	for alien_row in range(number_rows):
		for alien_number in range(number_alien_x):
			create_alien(ai_settings, screen, aliens, alien_number, alien_row)

def check_fleet_edges(ai_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_factor
	ai_settings.fleet_direction *= -1
	
def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
	
	check_fleet_edges(ai_settings, aliens)
	
	aliens.update()
	
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
		
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
	
	stats.score = 0
	sb.prep_score()
	if stats.ship_left > 0:
		
		stats.ship_left -= 1
		sb.prep_ships()
		
		aliens.empty()
		bullets.empty()	
		
		ship.center_ship()
		create_fleet(ai_settings, screen, aliens, ship)
		
	else:
		with open("stats.txt","w") as ss:
			ss.write(str(stats.highest_score))
		aliens.empty()
		bullets.empty()
		stats.game_active = False
		pygame.mouse.set_visible(True)
	
	
	sleep(1)
	
def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
			break
	
			
def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, sb):
	
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	sb.show_score()
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()

