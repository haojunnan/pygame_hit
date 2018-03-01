#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
	"""�Էɴ��ӵ����й������"""
	
	def __init__(self,al_settings,screen,fly):
		"""�ڷɴ�λ�ô���һ���ӵ�����"""
		super(Bullet,self).__init__()
		self.screen = screen
		
		#��(0,0)�����������ӵ�����������ȷλ��
		self.rect = pygame.Rect(0,0,al_settings.bullet_width,
		al_settings.bullet_height)		# #pygame.Rect(left,top,width,height)
		self.rect.centerx = fly.rect.centerx
		self.rect.top = fly.rect.top
		
		#�洢��С����ʾ�ӵ���λ��
		self.y = float(self.rect.y)
		
		self.color = al_settings.bullet_color
		self.speed = al_settings.bullet_speed
	def update(self):
		"""�����ƶ��ӵ�"""
		#���±�ʾ�ӵ�λ�õ�С��ֵ
		self.y -= self.speed
		self.rect.y = self.y 
	def draw_bullet(self):
		"""����Ļ�ϻ����ӵ�"""
		pygame.draw.rect(self.screen,self.color,self.rect)
