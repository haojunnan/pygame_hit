#coding:gb2312
import pygame
import game_function as gf
from settings import Settings
from fly import Fly
from pygame.sprite import Group
from aline import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()  #初始化pygame
	al_settings = Settings()
	screen = pygame.display.set_mode((al_settings.screen_width,
	al_settings.screen_height))   #创建一个窗口
	pygame.display.set_caption("Alien Invasion")    #设置窗口标题
	#创建一个plat按钮
	play_button = Button(al_settings,screen,"Play")
	#创建一个用于储存游戏统计信息的实例
	stats = GameStats(al_settings)
	#创建一艘飞船,外星人
	fly = Fly(al_settings,screen)
	#alien = Alien(al_settings,screen)
	#创建用于储存子弹的编组，外星人编组组
	bullets = Group()
	aliens = Group()
	scoreboard = Scoreboard(al_settings,screen,stats)
	#创建外星人群
	gf.creat_fleet(al_settings,screen,aliens,fly)
	#开始主循环
	while True:
		#监视键盘鼠标事件
		gf.check_events(al_settings,screen,aliens,fly,bullets,stats,
		play_button,scoreboard)
		#for event in pygame.event.get(): 
		#	if event.type == pygame.QUIT:
		#		sys.exit()
		if stats.game_active:
			fly.update()
			gf.update_bullets(al_settings,screen,aliens,fly,bullets,
				stats,scoreboard)
			gf.update_aliens(al_settings,stats,screen,fly,aliens,bullets,
				scoreboard)
	#	bullets.update()
		#删除消失的子弹
	#	for bullet in bullets.copy():
	#		if bullet.rect.bottom <= 0:
	#			bullets.remove(bullet)
		#更新屏幕
		gf.update_screen(al_settings,screen,fly,bullets,aliens,stats,
			play_button,scoreboard)
		#screen.fill(al_settings.bg_color)
		#ship.blitme() #绘制飞船
		#让最近绘制的屏幕可见
		#pygame.display.flip()#和display.update()功能一样，update可传参
		
run_game()
