#coding:gb2312
class GameStats():
	"""跟踪游戏的统计信息"""
	def __init__(self,al_settings):
		"""初始化统计信息"""
		self.al_settings = al_settings
		self.reset_stats()
		self.game_active = False
		self.high_score = 0 
	def reset_stats(self):
		"""初始化在游戏运行期间可能变化的统计信息"""
		self.flys_left = self.al_settings.fly_limit
		self.score = 0
		self.alien_level = 1
