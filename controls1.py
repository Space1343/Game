import pygame
import sys
import time

from bullet import Bullet
from enemy1 import Enemy1

pygame.mixer.init()
pygame.mixer.pre_init(44100,-16,2,512)
piy = pygame.mixer.Sound("piy.ogg")
died = pygame.mixer.Sound("DiedOU.ogg")

def events(screen, gun, bullets):
    """Обработак событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
    #        elif event.key == pygame.K_w:
    #            gun.mup = True
    #        elif event.key == pygame.K_s:
    #            gun.mdown = True
            elif event.key == pygame.K_SPACE:
                piy.play()
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False
    #        elif event.key == pygame.K_w:
    #            gun.mup = False
    #        elif event.key == pygame.K_s:
    #            gun.mdown = False


def update(bg_color, screen, gun, enemies, bullets):
    """Экран"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemies.draw(screen)
    pygame.display.flip()


def update_bullets(screen, enemies, bullets):
    """Обновление позиции пули"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pygame.sprite.groupcollide(bullets, enemies, True, True)
    if len(enemies) == 0:
        bullets.empty()
        create_army(screen, enemies)

def gun_kill(stats, screen, gun, enemies, bullets):
    """Столкновение пушки и армии"""
    stats.guns_left -= 1
    enemies.empty()
    bullets.empty()
    create_army(screen, enemies)
    gun.create_gun()
    time.sleep(1)


def update_enemies(stats, screen, gun, enemies, bullets):
    """Обновление противников"""
    enemies.update()
    if pygame.sprite.spritecollideany(gun, enemies, ):
        gun_kill(stats, screen, gun, enemies, bullets)
    enemies_check(stats, screen, gun, enemies, bullets)


def enemies_check(stats, screen, gun, enemies, bullets):
    """Край экрана"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, enemies, bullets)
            break


def create_army(screen, enemies):
    """АРМИЯ"""
    enemy = Enemy1(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((800 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((600 - 100 - 2 * enemy_height) / enemy_height)

    for row_number in range(number_enemy_y - 3):
        for enemy_number in range(number_enemy_x):
            enemy = Enemy1(screen)
            enemy.x = enemy_width + (enemy_width * enemy_number)
            enemy.y = enemy_height + (enemy_height * row_number)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + 1.25 * (enemy.rect.height * row_number)
            enemies.add(enemy)
