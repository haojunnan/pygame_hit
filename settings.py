#coding:gb2312
class Settings():
	"""���桶���������ֵ����������õ��ࡷ"""
	def __init__(self):
		"""��ʼ����Ϸ����"""
		#��Ļ����
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230,230,230)
		self.speed = 0.4
		self.bullet_speed = 0.5
		self.bullet_width = 4
		self.bullet_height = 18
		self.bullet_color = (120,120,60)
		self.bullets_allowed = 5
		self.fleet_drop_speed = 8
		self.fleet_direction = -1
		self.fly_speed_factor = 1.5
		self.fly_limit = 3
		self.reset_massages()
	def live_up(self):
		self.alien_speed *= 2
		self.alien_points += 10
	def reset_massages(self):
		self.alien_speed = 0.3
		self.alien_points = 50
