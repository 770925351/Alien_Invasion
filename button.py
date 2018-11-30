import pygame.font
''' Play按钮类 '''
class Button():
    ''' 初始化按钮的各项参数 '''
    def __init__(self,ai_settings,screen,msg):
        self.screen = screen # 当前屏幕
        self.screen_rect = screen.get_rect() # 当前屏幕图形对象
        self.width = 200    # 按钮宽
        self.height = 50    # 按钮高
        self.button_color = (0,255,0)   # 按钮颜色
        self.text_color = (255,255,255) # 按钮文本字体颜色
        self.font = pygame.font.SysFont("arial",48) # 按钮字体
        self.rect = pygame.Rect(0,0,self.width,self.height) # 创建按钮图形对象
        self.rect.center = self.screen_rect.center  # 设置按钮位置
        self.prep_msg(msg) # 准备按钮文本
    ''' 准备按钮文本 '''
    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    ''' 显示按钮 '''
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)