#coding:gb2312
import pygame
import pygame.font
from pygame.sprite import Group
from fly import Fly
class Scoreboard():
	"""显示得分信息的类"""
	def __init__(self,al_settings,screen,stats):
		"""初始化显示得分涉及的属性"""
		self.screen = screen 
		self.al_settings = al_settings
		self.screen_rect = self.screen.get_rect()
		self.al_settings = al_settings
		self.stats = stats
		#显示得分信息是使用的字体设置
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		#准备初始得分图像
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_flys()
	def prep_score(self):
		"""将得分转化成换为一幅渲染的图像"""
		rounded_score = int(round(self.stats.score,-1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str,True,
			self.text_color,self.al_settings.bg_color)
		#将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 10
		self.score_rect.top = 0
	def prep_high_score(self):
		"""将最高分转换成一幅渲染图像"""
		high_score = int(round(self.stats.high_score,-1))
		high_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_str,True,
		self.text_color,self.al_settings.bg_color)
		#将最高分绘制到屏幕中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.screen_rect.top
	def prep_level(self):
		"""将等级转换成一幅渲染图像"""
		self.level_image = self.font.render(str(self.stats.alien_level),True,
			self.text_color,self.al_settings.bg_color)
		#将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom 
	def prep_flys(self):
		"""显示剩余飞船数"""
		self.flys = Group()
		for fly_number in range(self.stats.flys_left):
			fly = Fly(self.al_settings,self.screen)
			fly.rect.x = fly_number * fly.rect.width
			fly.rect.top  = 0
			self.flys.add(fly)
	def show_score(self):
		"""绘制图表"""
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image,self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.flys.draw(self.screen)
