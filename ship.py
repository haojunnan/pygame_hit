#coding:gb2312
import pygame
class Ship():
	def __init__(self,screen):
		"""��ʼ���ɻ�ͼ�����ó�ʼλ��"""
		self.screen = screen
		
		#���طɴ�ͼ�񲢻�ȡ����Ӿ���
		self.image = pygame.image.load('temple/ship.bmp')
		#surface���������ڱ�ʾͼ���ͼ��ֻҪָ���ߴ磬�Ϳ������ã�����ͨ��
		#load����ͼƬ�����ǿ����Զ�����һ��surface�������ͼ�񷵻ص�Ҳ��һ��surface����
		self.rect = self.image.get_rect()
		#surface.get_rect()���ص��ǵ���ʵ����Ϊsurface�����rect���� ����ȷ��λ��
		self.screen_rect = self.screen.get_rect() #��Ļ�������󴢴���screen_rect��
		#��ÿ���·ɴ���׼��Ļ�ײ�����   centerxΪ�����x����
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def blitme(self):
		"""��ָ��λ�û��Ʒɴ�"""
		self.screen.blit(self.image,self.rect)
		#blit(ͼ��λ��)
