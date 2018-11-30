''' 存储 '外星人入侵' 的所有设置的类 '''
class Settings():
    ''' 初始化游戏的设置 '''
    def __init__(self):
        # 屏幕相关参数
        self.screen_width = 1200      # 屏幕宽度
        self.screen_height = 700      # 屏幕高度
        self.bg_color = (230,230,230) # 背景颜色
        # 飞船相关参数
        self.ship_speed_factor = 1.5  # 飞船移动速度
        self.ship_limit = 3           # 飞船数量
        # 子弹相关参数
        self.bullet_speed_factor = 3  # 子弹飞行速度
        self.bullet_width =  3        # 子弹宽度
        self.bullet_height = 15       # 子弹高度
        self.bullet_color = 60,60,60  # 子弹颜色
        self.bullet_allowed = 3       # 子弹限制数量
        #外星人相关参数
        self.alien_speed_factor = 1   # 外星人左右移动速度
        self.fleet_drop_speed = 10    # 外星人下落速度
        self.fleet_direction = 1      # 外星人左右移动方向 1为向右 -1为向左
        # 加快游戏节奏
        self.speedup_scale = 1.1      # 增快飞船移动速度的速率
        self.score_scale = 1.5        # 增快分数随着游戏等级的提高的速率
    ''' 重置游戏难度 '''
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5  # 恢复默认飞船速度
        self.bullet_speed_factor = 3  # 恢复默认子弹速度
        self.alien_speed_factor = 1   # 恢复默认外星人移动速度
        self.fleet_direction = 1      # 恢复默认外星人移动方向
        self.alien_points = 50        # 恢复每个外星人初始的分数
    ''' 增加游戏难度 '''
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale    # 加快飞船移动速度
        self.bullet_speed_factor *= self.speedup_scale  # 加快子弹飞行速度
        self.alien_speed_factor *= self.speedup_scale   # 加快外星人移动速度
        self.alien_points = int(self.alien_points * self.score_scale) #提高每个外星人分数