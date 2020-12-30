import sys

import pygame
from bullet import Bullet
from alien import Alien


def create_fleet(ai_settings, screen, aliens):
    # 创建外星人群
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width

    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))

    # 创建第一个外星人
    for alien_number in range(number_alien_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add_internal(alien)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建子弹并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    # 响应松开
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    # 响应案件和鼠标事件

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 更新屏幕上的图像， 并切换到新屏幕
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    ship.blitme()
    aliens.draw(screen)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 让最近的绘制屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹的位置，并删除已消失的自动那
    bullets.update()

    # 删除消失的子弹
    for bullet in bullets.copy():  # 不能直接从编组中删除条目，必须必须遍历编组的副本
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
