
class Settings():
	def __init__(self):
		
		
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		
		self.ship_limit = 3
		
		
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color =(60,60,60)
		self.bullet_allowed = 5
		
		
		self.fleet_drop_factor = 10
		
		
		self.speedup_scale = 1.1
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 5
		self.alien_speed_factor = 0.5
		self.alien_point = 50
		
		self.fleet_direction = 1
		
	def increase_speed(self):
		
		self.ship_speed_factor *= self.speedup_scale 
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.alien_point = int(self.alien_point * self.speedup_scale)