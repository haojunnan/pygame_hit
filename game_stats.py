#coding:gb2312
class GameStats():
	"""������Ϸ��ͳ����Ϣ"""
	def __init__(self,al_settings):
		"""��ʼ��ͳ����Ϣ"""
		self.al_settings = al_settings
		self.reset_stats()
		self.game_active = False
		self.high_score = 0 
	def reset_stats(self):
		"""��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����Ϣ"""
		self.flys_left = self.al_settings.fly_limit
		self.score = 0
		self.alien_level = 1
