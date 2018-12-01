import pygame.font

from ship import Ship

from pygame.sprite import Group

class Scoreboard():
	
	def __init__(self, ai_settings, screen, stats):
		
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		
		self.font = pygame.font.SysFont('Microsoft YaHei', 25)
		self.text_color = (30,30,30)
		
		
		self.prep_highest_score()
		self.prep_level()
		self.prep_score()
		self.prep_ships()
	
	def prep_score(self):
		
		score_str = '得分：' + '{:,}'.format(int(round(self.stats.score,-1)))
		self.image_score = self.font.render(score_str, True ,
			self.text_color, self.ai_settings.bg_color)
		
		
		self.image_score_rect = self.image_score.get_rect()
		self.image_score_rect.right = self.image_level_rect.left -20
		self.image_score_rect.top = 10
		
	def prep_highest_score(self):
		
		highest_score_str = '最高分：' + '{:,}'.format(int(round(self.stats.highest_score,-1)))
		self.image_highest_score = self.font.render(highest_score_str, True ,
			self.text_color, self.ai_settings.bg_color)
		
		
		self.image_highest_score_rect = self.image_highest_score.get_rect()
		self.image_highest_score_rect.centerx = self.screen_rect.centerx
		self.image_highest_score_rect.top = 10
		
	def prep_level(self):
		
		level_str = '等级：' + str(self.stats.level)
		self.image_level = self.font.render(level_str, True ,
			self.text_color, self.ai_settings.bg_color)
		
		
		self.image_level_rect = self.image_level.get_rect()
		self.image_level_rect.right = self.screen_rect.right -20
		self.image_level_rect.top = 10
	
	def prep_ships(self):
		
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.image = pygame.transform.scale(ship.image,(30,30))
			ship.rect = ship.image.get_rect()
			ship.rect.left = 20 + ship.rect.width * ship_number
			ship.rect.top = 15 
			
			self.ships.add(ship)
		
	def show_score(self):
		
		self.screen.blit(self.image_score, self.image_score_rect)
		self.screen.blit(self.image_highest_score, self.image_highest_score_rect)
		self.screen.blit(self.image_level, self.image_level_rect)
		self.ships.draw(self.screen)
