#coding:gb2312
import pygame
import pygame.font
from pygame.sprite import Group
from fly import Fly
class Scoreboard():
	"""��ʾ�÷���Ϣ����"""
	def __init__(self,al_settings,screen,stats):
		"""��ʼ����ʾ�÷��漰������"""
		self.screen = screen 
		self.al_settings = al_settings
		self.screen_rect = self.screen.get_rect()
		self.al_settings = al_settings
		self.stats = stats
		#��ʾ�÷���Ϣ��ʹ�õ���������
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		#׼����ʼ�÷�ͼ��
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_flys()
	def prep_score(self):
		"""���÷�ת���ɻ�Ϊһ����Ⱦ��ͼ��"""
		rounded_score = int(round(self.stats.score,-1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str,True,
			self.text_color,self.al_settings.bg_color)
		#���÷ַ�����Ļ���Ͻ�
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 10
		self.score_rect.top = 0
	def prep_high_score(self):
		"""����߷�ת����һ����Ⱦͼ��"""
		high_score = int(round(self.stats.high_score,-1))
		high_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_str,True,
		self.text_color,self.al_settings.bg_color)
		#����߷ֻ��Ƶ���Ļ����
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top
	def prep_level(self):
		"""���ȼ�ת����һ����Ⱦͼ��"""
		self.level_image = self.font.render(str(self.stats.alien_level),True,
			self.text_color,self.al_settings.bg_color)
		#���ȼ����ڵ÷��·�
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom 
	def prep_flys(self):
		"""��ʾʣ��ɴ���"""
		self.flys = Group()
		for fly_number in range(self.stats.flys_left):
			fly = Fly(self.al_settings,self.screen)
			fly.rect.x = fly_number * fly.rect.width
			fly.rect.top  = 0
			self.flys.add(fly)
	def show_score(self):
		"""����ͼ��"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.flys.draw(self.screen)
