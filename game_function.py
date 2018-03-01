#coding:gb2312
import pygame
import sys
from bullet import Bullet
from aline import Alien
from time import sleep
def key_down(event,al_settings,screen,fly,bullets):
	if event.key == pygame.K_RIGHT:
		fly.moving_right = True
	elif event.key == pygame.K_LEFT:
		fly.moving_left = True
	elif event.key == pygame.K_UP:
		fly.moving_up = True
	elif event.key == pygame.K_DOWN:
		fly.moving_down = True
	elif event.key == pygame.K_SPACE:
		#创建一颗子弹，将其加入编组中
		if len(bullets) < al_settings.bullets_allowed:
			new_bullet = Bullet(al_settings,screen,fly)
			bullets.add(new_bullet)
def key_up(event,fly):
	if event.key == pygame.K_RIGHT:
		fly.moving_right = False
	elif event.key == pygame.K_LEFT:
		fly.moving_left = False
	elif event.key == pygame.K_UP:
		fly.moving_up = False
	elif event.key == pygame.K_DOWN:
		fly.moving_down = False
def play_game(al_settings,screen,aliens,fly,stats,play_button,bullets,
	mouse_x,mouse_y,scoreboard):
	if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
		start_game(al_settings,screen,aliens,fly,stats,bullets,scoreboard)
def start_game(al_settings,screen,aliens,fly,stats,bullets,scoreboard):
		#重置记分信息
		pygame.mouse.set_visible(False)
		sleep(0.5)
		stats.reset_stats()
		stats.game_active = True
		scoreboard.prep_flys()
		scoreboard.prep_score()
		scoreboard.prep_level()
		#清空外星人列表和子弹列表
		bullets.empty()
		aliens.empty()
		#创建一群新的外星人，并让飞船居中
		creat_fleet(al_settings,screen,aliens,fly)
		al_settings.reset_massages()
		fly.center_fly()
def check_events(al_settings,screen,aliens,fly,bullets,stats,play_button,
	scoreboard):
	"""响应事件和鼠标事件"""
	for event in pygame.event.get():
		"""按键控制飞船左右移"""
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			key_down(event,al_settings,screen,fly,bullets)
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			elif event.key == pygame.K_p:
				start_game(al_settings,screen,aliens,fly,stats,bullets,
					scoreboard)
		#	if event.key == pygame.K_RIGHT:
		#		fly.moving_right = True
		#	elif event.key == pygame.K_LEFT:
		#		fly.moving_left = True
		#	elif event.key == pygame.K_UP:
		#		fly.moving_up = True
		#	elif event.key == pygame.K_DOWN:
		#		fly.moving_down = True
		elif event.type == pygame.KEYUP:
			key_up(event,fly)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			play_game(al_settings,screen,aliens,fly,stats,play_button,
			bullets,mouse_x,mouse_y,scoreboard)
			#fly.moving_right = False
			#fly.moving_left = False
			#fly.moving_up = False
			#fly.moving_down = False

def update_screen(al_settings,screen,fly,bullets,aliens,stats,
	play_button,scoreboard):
	"""刷新界面"""
	screen.fill(al_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	fly.blitme()
	aliens.draw(screen)
	scoreboard.show_score()
	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()
def check_high_score(stats,scoreboard):
	"""检查是否有新的最高分"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		scoreboard.prep_high_score()
def update_bullets(al_settings,screen,aliens,fly,bullets,stats,scoreboard):
	"""检查子弹是否跑出屏幕，跑出则删除"""
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(al_settings,screen,aliens,fly,bullets,
		stats,scoreboard)
def check_bullet_alien_collisions(al_settings,screen,aliens,fly,bullets,
	stats,scoreboard):
	"""相应子弹外星人碰撞"""
	#检查是否击中外星人，如果击中，删除该子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	#每有一个外星人被击中，记一次分
	if collisions:
		for aliens in collisions.values():
			stats.score += al_settings.alien_points * len(aliens)
			scoreboard.prep_score()
		check_high_score(stats,scoreboard)
	if len(aliens) == 0:
		#删除现有的子弹并新建一群外星人
		bullets.empty()
		al_settings.live_up()
		stats.alien_level += 1
		scoreboard.prep_level()
		creat_fleet(al_settings,screen,aliens,fly)
def get_number_alien(al_settings,alien_width):
	avaiable_space = al_settings.screen_width - 2*alien_width
	number_aliens = int(avaiable_space / (2*alien_width))
	return number_aliens
def get_number_rows(al_settings,fly_height,alien_height):
	"""计算可容纳多少行外星人"""
	available_space_y = (al_settings.screen_height - (3 * alien_height)
	- fly_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows
def creat_alien(al_settings,screen,number_aliens,aliens,row_number):
	"""创建外星人"""
	alien = Alien(al_settings,screen)
	alien.width = alien.rect.width
	alien.x = alien.width + 2 * alien.width * number_aliens
	alien.rect.x = alien.x
	alien.y = alien.rect.height + 2 * alien.rect.height * row_number
	alien.rect.y = alien.y
	aliens.add(alien)
def creat_fleet(al_settings,screen,aliens,fly):
	"""创建外星人群"""
	#创建一个外星人，计算可容纳多少外星人
	alien = Alien(al_settings,screen)
	number_aliens = get_number_alien(al_settings,alien.rect.width)
	number_rows = get_number_rows(al_settings,fly.rect.height,
	alien.rect.height)
 	#创建外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens):
			creat_alien(al_settings,screen,alien_number,aliens,row_number)
def check_fleet_edge(al_settings,aliens):
	"""有外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(al_settings,aliens)
			break
def change_fleet_direction(al_settings,aliens):
	"""使飞船下移并改变方向"""
	for alien in aliens.sprites():
		alien.rect.y += al_settings.fleet_drop_speed
	al_settings.fleet_direction *= -1
def update_aliens(al_settings,stats,screen,fly,aliens,bullets,scoreboard):
	"""更新外星人位置"""
	check_fleet_edge(al_settings,aliens)
	aliens.update()
	#检测外星人和飞机的碰撞
#	if pygame.sprite.spritecollideany(fly,aliens):
	#	print("ship hit！")
	#检测外星人和飞船碰撞
	if pygame.sprite.spritecollideany(fly,aliens):
		fly_hit(al_settings,stats,screen,fly,aliens,bullets,scoreboard)
	check_aliens_bottom(al_settings,stats,screen,fly,aliens,bullets,scoreboard)
def fly_hit(al_settings,stats,screen,fly,aliens,bullets,scoreboard):
	"""相应被外星人撞到的飞船"""
	if stats.flys_left > 0:
		#将ships_left减1
		stats.flys_left -= 1
		scoreboard.prep_flys()
		#情空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()
		#创建一群新的外星人，并将飞船放到屏幕底端中央
		creat_fleet(al_settings,screen,aliens,fly)
		fly.center_fly()
		#暂停
		sleep(0.5)
	else:
		pygame.mouse.set_visible(True)
		stats.game_active = False
def check_aliens_bottom(al_settings,stats,screen,fly,aliens,bullets,scoreboard):
	"""检查是否有外星人到达屏幕底端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#像飞船被撞到一样
			fly_hit(al_settings,stats,screen,fly,aliens,bullets,scoreboard)
			break
