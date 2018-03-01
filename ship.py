#coding:gb2312
import pygame
class Ship():
	def __init__(self,screen):
		"""初始化飞机图像并设置初始位置"""
		self.screen = screen
		
		#加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('temple/ship.bmp')
		#surface对象是用于表示图像的图像，只要指定尺寸，就可以利用，可以通过
		#load加载图片或者是可以自动创建一个surface对象加载图像返回的也是一个surface对象
		self.rect = self.image.get_rect()
		#surface.get_rect()返回的是调用实例即为surface对象的rect对象 用于确定位置
		self.screen_rect = self.screen.get_rect() #屏幕创建对象储存在screen_rect中
		#将每艘新飞船对准屏幕底部中央   centerx为对象的x坐标
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	
	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)
		#blit(图像，位置)
