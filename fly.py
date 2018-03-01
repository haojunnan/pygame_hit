#coding:gb2312
import pygame
from pygame.sprite import Sprite
class Fly(Sprite):
	def __init__(self,al_settings,screen):
		"""设置飞船的图像和位置"""
		super(Fly,self).__init__()
		self.screen = screen
		self.al_settings = al_settings
		self.image = pygame.image.load('ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)
	def update(self):
		"""根据moving_right状态调整飞机位置"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.al_settings.speed
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.al_settings.speed
		elif self.moving_up and self.rect.top > 0:
			self.bottom -= self.al_settings.speed
		elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.bottom += self.al_settings.speed
		self.rect.centerx = self.center
		self.rect.bottom = self.bottom
	def blitme(self):
		self.screen.blit(self.image,self.rect)
	def center_fly(self):
		"""让飞船居中"""
		self.center = self.screen_rect.centerx
		self.bottom = self.screen_rect.bottom
		self.rect.bottom = self.bottom
