#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	"""对飞船子弹进行管理的类"""
	
	def __init__(self,al_settings,screen,fly):
		"""在飞船位置创建一个子弹对象"""
		super(Bullet,self).__init__()
		self.screen = screen
		
		#在(0,0)处创建矩形子弹，并设置正确位置
		self.rect = pygame.Rect(0,0,al_settings.bullet_width,
		al_settings.bullet_height)		# #pygame.Rect(left,top,width,height)
		self.rect.centerx = fly.rect.centerx
		self.rect.top = fly.rect.top
		
		#存储用小数表示子弹的位置
		self.y = float(self.rect.y)
		
		self.color = al_settings.bullet_color
		self.speed = al_settings.bullet_speed
	def update(self):
		"""向上移动子弹"""
		#更新表示子弹位置的小数值
		self.y -= self.speed
		self.rect.y = self.y 
	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen,self.color,self.rect)
