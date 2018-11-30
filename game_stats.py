class GameStats():

    ''' 初始化游戏状态的每个属性 '''
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings  # 将游戏的设置参数传进来
        self.reset_stats()              # 重置游戏状态
        self.game_active = False        # 游戏刚开始的状态为关闭,不执行
        with open("high_score.txt") as file : # 初始化最高分,从文件中读取
            self.high_score = int(file.read())
    ''' 重置游戏状态 '''
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit   # 将设置中的飞船限定数量传进来
        self.score = 0                                  # 将所得分数初始化为0
        self.level = 1                                  # 将游戏级别初始化为1