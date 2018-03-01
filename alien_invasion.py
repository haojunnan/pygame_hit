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
	# ��ʼ����Ϸ������һ����Ļ����
	pygame.init()  #��ʼ��pygame
	al_settings = Settings()
	screen = pygame.display.set_mode((al_settings.screen_width,
	al_settings.screen_height))   #����һ������
	pygame.display.set_caption("Alien Invasion")    #���ô��ڱ���
	#����һ��plat��ť
	play_button = Button(al_settings,screen,"Play")
	#����һ�����ڴ�����Ϸͳ����Ϣ��ʵ��
	stats = GameStats(al_settings)
	#����һ�ҷɴ�,������
	fly = Fly(al_settings,screen)
	#alien = Alien(al_settings,screen)
	#�������ڴ����ӵ��ı��飬�����˱�����
	bullets = Group()
	aliens = Group()
	scoreboard = Scoreboard(al_settings,screen,stats)
	#����������Ⱥ
	gf.creat_fleet(al_settings,screen,aliens,fly)
	#��ʼ��ѭ��
	while True:
		#���Ӽ�������¼�
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
		#ɾ����ʧ���ӵ�
	#	for bullet in bullets.copy():
	#		if bullet.rect.bottom <= 0:
	#			bullets.remove(bullet)
		#������Ļ
		gf.update_screen(al_settings,screen,fly,bullets,aliens,stats,
			play_button,scoreboard)
		#screen.fill(al_settings.bg_color)
		#ship.blitme() #���Ʒɴ�
		#��������Ƶ���Ļ�ɼ�
		#pygame.display.flip()#��display.update()����һ����update�ɴ���
		
run_game()
