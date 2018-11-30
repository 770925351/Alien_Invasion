import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from button import Button
from scoreboard import ScoreBoard
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_funtions as gf


def run_game():
    ai_settings = Settings() # 初始化设置参数
    screen = gf.init(ai_settings) # 初始化屏幕
    stats = GameStats(ai_settings) # 初始化游戏状态信息
    sb = ScoreBoard(ai_settings,screen,stats) # 初始化记分牌信息
    play_button = Button(ai_settings,screen,"Play") # 初始化按钮
    ship = Ship(ai_settings,screen)     # 初始化飞船
    aliens = Group()    # 初始化外星人组
    bullets = Group()   # 初始化子弹组
    gf.create_fleet(ai_settings,screen,aliens,ship) # 创建外星人

    while True :
        ''' 循环检测事件 '''
        gf.check_events(ship,ai_settings,screen,aliens,bullets,play_button,stats,sb)
        ''' 如果游戏开始,则不断更新子弹,飞船,外星人的位置 '''
        if stats.game_active :
                ship.update()
                gf.update_bullets(ai_settings,screen,aliens,bullets,ship,stats,sb)
                gf.updete_aliens(ai_settings,stats,screen,bullets,aliens,ship,sb)
        ''' 刷新所有屏幕信息 '''
        gf.update_screen(ai_settings,stats,screen,ship,bullets,aliens,play_button,sb)
                
run_game()
