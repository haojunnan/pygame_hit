#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	"""����������"""
	def __init__(self,al_settings,screen):
		"""��ʼ�������˼�ȷ����ʼλ��"""	
		super(Alien,self).__init__()
		self.screen = screen
		self.al_settings = al_settings
		#����������ͼ�Σ�����rectͼ��
		self.image = pygame.image.load("alien.bmp")
		self.rect = self.image.get_rect()
		#ÿ�����������������Ļ���ϽǸ���
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#��ָ��λ�û���������
		self.x = float(self.rect.x)
#	def blitme(self):
		"""��ָ��λ�û���������"""
	#	self.screen.blit(self.image,self.rect)
	def check_edges(self):
		"""�ж��������Ƿ񴥵���Ե"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= screen_rect.left:
			return  True
	def update(self):
		"""�����ƶ�������"""
		self.x += (self.al_settings.alien_speed * 
		self.al_settings.fleet_direction)
		self.rect.x = self.x
		
