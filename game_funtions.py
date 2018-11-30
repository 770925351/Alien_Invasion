import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien
''' 窗口屏幕初始化,返回一个surface '''
def init(ai_settings):
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
    pygame.display.set_caption("Alien Invasion") # 设置窗口标题
    return screen
''' 开火方法,限定屏幕中存在最大数量的子弹数目'''
def fire_bullet(ai_settings,screen,bullets,ship):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
''' 当接收到按键按下信号时的处理方法'''        
def check_keydown_events(event,ship,ai_settings,screen,bullets,aliens,stats,sb):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True       # 长按右键设置飞船一直向右状态
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True        # 长按左键设置飞船一直向左状态 
    elif event.key == pygame.K_UP:
        ship.moving_up = True          # 长按上键设置飞船一直向上状态
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True        # 长按下键设置飞船一直向下状态
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,bullets,ship)    # 空格开火
    elif event.key == pygame.K_p:      # p键开始游戏和重置游戏
        with open("high_score.txt","w") as file :   # 开始游戏之前把当前最高分数写入文件
            file.write(str(stats.high_score))
        ai_settings.initialize_dynamic_settings()   # 重置游戏难度参数
        start_game(ai_settings,screen,aliens,bullets,ship,stats,sb) #开始游戏
    elif event.key == pygame.K_q:      # 退出游戏
        with open("high_score.txt","w") as file :   # 退出游戏之前写入当前最高分数
            file.write(str(stats.high_score))
        sys.exit()
''' 当接收到按键弹起信号时的处理方法'''
def check_keyup_events(event,ship):    
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False 
''' 检查当前是否有事件发生 '''
def check_events(ship,ai_settings,screen,aliens,bullets,play_button,stats,sb):
    ''' 响应按键和鼠标事件 '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 退出信号,将最高分写入并退出
            with open("high_score.txt","w") as file :
                file.write(str(stats.high_score))
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 按键按下信号
            check_keydown_events(event,ship,ai_settings,screen,bullets,aliens,stats,sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)  # 按键抬起信号
        elif event.type == pygame.MOUSEBUTTONDOWN: # 鼠标点击信号
            mouse_x , mouse_y = pygame.mouse.get_pos() # 获取鼠标点击的x,y坐标
            ''' 查看是否点击到了Play按钮 '''
            check_play_button(ai_settings,screen,ship,aliens,bullets,stats,play_button,mouse_x,mouse_y,sb)
''' 刷新当前屏幕信息 '''
def update_screen(ai_settings,stats,screen,ship,bullets,aliens,play_button,sb):
    ''' 更新屏幕 '''
    screen.fill(ai_settings.bg_color) # 显示整个屏幕
    for bullet in bullets.sprites() : # 显示子弹
        bullet.draw_bullet()
    aliens.draw(screen) # 显示外星人
    ship.blitme()       # 显示飞船
    sb.show_score()     # 显示记分牌
    if stats.game_active == False : # 如果是第一次打开游戏,显示play按钮
        play_button.draw_button()
    pygame.display.flip()             #刷新整个界面

''' 刷新子弹位置 '''
def update_bullets(ai_settings,screen,aliens,bullets,ship,stats,sb):
    bullets.update()
    for bullet in bullets.copy(): # 如果子弹飞出屏幕外就删除它
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    ''' 检查子弹是否击中外星人 '''
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb)
''' 刷新外星人位置 '''
def updete_aliens(ai_settings,stats,screen,bullets,aliens,ship,sb):
    check_fleet_edges(ai_settings,aliens) # 检查外星人排组是否移动到屏幕边缘
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens): # 如果外星人与飞船相撞,game over
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb) # 如果外星人到达屏幕底部,game over
''' 获取当前屏幕能容下几个外星人 '''
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x/(2 * alien_width))
    return number_alien_x
''' 获取当前屏幕能容下几排外星人 '''
def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
''' 生成一排外星人 '''
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
''' 生成多排外星人 '''
def create_fleet(ai_settings,screen,aliens,ship):
    alien = Alien(ai_settings,screen)
    number_alien_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.width)
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
''' 检查外星人是否移动到屏幕边缘 '''
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
''' 改变外星人移动方向 '''
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
''' 检查子弹是否击中外星人 '''
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets,stats,sb):
    ''' 返回一个装有子弹和击中外星人的字典 '''
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True) 
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens) # 增加分数
        sb.prep_score() # 刷新分数
        check_high_score(stats,sb) # 更新最高分数
    if len(aliens) == 0 :   # 如果外星人全部被击杀,重新生成外星人,并提高游戏难度
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,aliens,ship)
''' 飞船碰到外星人或者外星人到达屏幕边缘 '''
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    if stats.ships_left > 0 :
        stats.ships_left -= 1
        sb.prep_ships()
    else : 
        stats.game_active = False
        pygame.mouse.set_visible(True)
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()
    sleep(0.5)
''' 外星人到达屏幕底部 '''
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)
            break
''' 点击play按钮开始游戏 '''
def check_play_button(ai_settings,screen,ship,aliens,bullets,stats,play_button,mouse_x,mouse_y,sb):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active :
        with open("high_score.txt","w") as file :
            file.write(str(stats.high_score))
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings,screen,aliens,bullets,ship,stats,sb)
''' 开始游戏 '''
def start_game(ai_settings,screen,aliens,bullets,ship,stats,sb):
    stats.reset_stats()
    stats.game_active = True
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings,screen,aliens,ship)
    ship.center_ship()
    pygame.mouse.set_visible(False)
''' 更新最高分数 '''
def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()