import pygame.font
from pygame.sprite import Group
from ship import Ship

''' 显示得分信息 '''
class ScoreBoard():

    ''' 初始化显示得分涉及的属性 '''
    def __init__(self,ai_settings,screen,stats):
        # 基本属性
        self.screen = screen                    # 获取屏幕信息
        self.screen_rect = screen.get_rect()    # 获取屏幕形状信息
        self.ai_settings = ai_settings          # 获取游戏设置信息
        self.stats = stats                      # 获取游戏状态
        # 字体属性
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont("arial",30)
        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    ''' 将得分转换为图像并显示 '''
    def prep_score(self):

        ''' 下面两句将分数格式化,格式化成带逗号的形式 '''
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)

        ''' 初始化得分图像 '''
        self.score_image = self.font.render("Score:"+score_str,True,self.text_color,self.ai_settings.bg_color)

        ''' 获取得分牌图形对象并设置得分牌位置 '''
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    ''' 在屏幕显示记分牌 '''
    def show_score(self):
        # 显示记分牌的分数
        self.screen.blit(self.score_image,self.score_rect)
        # 显示记分牌的最高分
        self.screen.blit(self.high_score_image,self.high_score_rect)
        # 显示记分牌的当前游戏难度级别
        self.screen.blit(self.level_image,self.level_rect)
        # 显示记分牌的飞船数量,即你的命数
        self.ships.draw(self.screen)

    ''' 准备最高分的图像并显示 '''    
    def prep_high_score(self):
        ''' 下面两句将分数格式化,格式化成带逗号的形式 '''
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        ''' 生成最高分的图像并获取他的图形对象 '''
        self.high_score_image = self.font.render("High Score:"+high_score_str,True,self.text_color,self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        ''' 设置最高分显示的位置 '''
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    ''' 准备游戏级别的图像并显示 '''
    def prep_level(self):
        ''' 生成游戏级别的图像并获得其图形对象 '''
        self.level_image = self.font.render("Level "+str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        ''' 设置游戏级别显示的位置 '''
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    ''' 准备飞船的图像并显示 '''
    def prep_ships(self):
        # 新建一个ship的组
        self.ships = Group()
        # 循环迭代,新建每个飞船,添加到组中,并设置其显示位置
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)