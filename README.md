# Python 外星人入侵小游戏开发
> 代码思路和架构均来自于 **Python编程:从入门到实践 [Eric Matthes]**
## 1.运行环境
> Python3.5 + Pygame
## 2.安装Pygame
- Windows
> - 安装Python3.5 
[Python3.5下载地址](https://www.python.org/ftp/python/3.5.4/python-3.5.4.exe)
> - 下载Pygame
[Pygame下载地址](https://bitbucket.org/pygame/pygame/downloads/pygame-1.9.2-cp35-cp35m-win32.whl)
> - 安装Pygame
> ```
> python -m pip install --user pygame-1.9.2-cp35-cp35m-win32.whl
> ```
- Linux 
> ```
> sudo apt-get install python3-dev mercurial
> sudo apt-get install libsdl-image1.2-dev libsdl2-dev libsdl-ttf2.0-dev
> sudo apt-get install libsdl-mixer1.2-dev libportmidi-dev
> sudo apt-get install libswscale-dev libsmpeg-dev libavformat-dev libavcode-dev
> sudo apt-get install python-numpy
> git clone https://github.com/pygame/pygame.git
> cd pygame
> python3 setup.py build
> sudo python3 setup.py install
> ```
## 3.游戏功能
> - 可记录最高分和当前分
> - 可记录当前飞船命数
> - 可记录当前游戏等级
## 4.操作简介
> **p**  重新开始游戏
> **↑↓←→** 上下左右移动飞船
> **q** 退出游戏
> **空格** 发射子弹
## 5.代码结构
- alien_invasion.py
> 游戏的运行文件,包含总体的运行流程及框架
- alien.py
> 定义外星人
- bullet.py
> 定义子弹
- ship.py
> 定义飞船
- button.py
> 定义Play按钮
- scoreboard.py
> 定义记分板
- settings.py
> 定义游戏的初始参数
- game_stats.py
> 定义游戏状态
- game_fuctions.py
> 定义游戏操作
- high_score.txt
> 存储游戏历史最高分数
## 6.小游戏截图
![游戏截图1](https://github.com/770925351/Alien_Invasion/blob/master/screenshot/1.png)

![游戏截图2](https://github.com/770925351/Alien_Invasion/blob/master/screenshot/2.png)

![游戏截图3](https://github.com/770925351/Alien_Invasion/blob/master/screenshot/3.png)

## 7.作者联系方式
- QQ:770925351
- 微信:tc770925351
- 邮箱:770925351@qq.com
