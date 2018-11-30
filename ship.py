import pygame
from pygame.sprite import Sprite

''' 飞船类 '''
class Ship(Sprite):
    ''' 初始化飞船各项参数 '''
    def __init__(self,ai_settings,screen):

        super().__init__()
        ''' 初始化飞船屏幕 '''
        self.screen = screen

        ''' 初始化飞船参数'''
        self.ai_settings = ai_settings

        ''' 加载飞船图片 '''
        self.image = pygame.image.load('images/ship.bmp')

        ''' 获取屏幕所占的矩形 '''
        self.screen_rect = screen.get_rect()

        ''' 获取飞船图片所占的矩形 '''
        self.rect = self.image.get_rect()

        ''' 将每艘飞船放在屏幕中央 '''
        self.rect.centerx = self.screen_rect.centerx # x坐标
        self.rect.bottom = self.screen_rect.bottom   # y坐标

        ''' 在飞船的属性中center中存储小数值'''
        self.center = float(self.rect.centerx)
        self.vertical = float(self.rect.bottom)

        ''' 初始化飞船的每个状态,如果为真,则是一直移动的状态'''
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
    def blitme(self):
        ''' 在指定位置绘制飞船 '''
        self.screen.blit(self.image,self.rect)     

    
    ''' 
        在这里的算法说明:飞船的每个状态代表着长按上下左右键,下面判断飞船位置是否超出主界面
        如果超出,则停止移动,如果不超出,则继续激动
    '''
    ''' 更新飞船位置 '''
    def update(self):
        if self.moving_left and self.rect.left > self.screen_rect.left :
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.vertical -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom :
            self.vertical += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.vertical
    ''' 将飞船放置在屏幕的正中间底部 '''
    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.vertical = self.screen_rect.bottom
