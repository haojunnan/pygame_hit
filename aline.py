#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	"""单个外星人"""
	def __init__(self,al_settings,screen):
		"""初始化外星人及确定初始位置"""	
		super(Alien,self).__init__()
		self.screen = screen
		self.al_settings = al_settings
		#加载外星人图形，设置rect图像
		self.image = pygame.image.load("alien.bmp")
		self.rect = self.image.get_rect()
		#每个外星人最初都在屏幕左上角附近
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#在指定位置绘制外星人
		self.x = float(self.rect.x)
#	def blitme(self):
		"""在指定位置绘制外星人"""
	#	self.screen.blit(self.image,self.rect)
	def check_edges(self):
		"""判断外星人是否触到边缘"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= screen_rect.left:
			return  True
	def update(self):
		"""向右移动外星人"""
		self.x += (self.al_settings.alien_speed * 
		self.al_settings.fleet_direction)
		self.rect.x = self.x
		
