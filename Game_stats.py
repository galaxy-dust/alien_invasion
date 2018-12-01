class GameStats():
	
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		
		
		self.read_highest_score()
	
	def read_highest_score(self):
		with open("stats.txt","r") as ss:	
			if ss.read():
				ss.seek(0)
				self.highest_score = int(ss.read())
			else:
				self.highest_score = 0

		
	def reset_stats(self):
		self.ship_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
		
