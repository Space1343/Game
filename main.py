import pygame
from pygame.sprite import Group

import controls1
import controls2
import controls3
import controls4
import controls5
from gun import Gun
from stats import Stats


def run1():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PUSHKA-XLOPUSHKA")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls1.create_army(screen, enemies)
    stats = Stats()

    while True:
        controls1.events(screen, gun, bullets)
        gun.update_gun()
        controls1.update(bg_color, screen, gun, enemies, bullets)
        controls1.update_bullets(screen,  enemies, bullets)
        controls1.update_enemies(stats, screen, gun, enemies, bullets)

def run2():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PUSHKA-XLOPUSHKA")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls2.create_army(screen, enemies)
    stats = Stats()

    while True:
        controls2.events(screen, gun, bullets)
        gun.update_gun()
        controls2.update(bg_color, screen, gun, enemies, bullets)
        controls2.update_bullets(screen,  enemies, bullets)
        controls2.update_enemies(stats, screen, gun, enemies, bullets)

def run3():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PUSHKA-XLOPUSHKA")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls3.create_army(screen, enemies)
    stats = Stats()

    while True:
        controls3.events(screen, gun, bullets)
        gun.update_gun()
        controls3.update(bg_color, screen, gun, enemies, bullets)
        controls3.update_bullets(screen,  enemies, bullets)
        controls3.update_enemies(stats, screen, gun, enemies, bullets)

def run4():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PUSHKA-XLOPUSHKA")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls4.create_army(screen, enemies)
    stats = Stats()

    while True:
        controls4.events(screen, gun, bullets)
        gun.update_gun()
        controls4.update(bg_color, screen, gun, enemies, bullets)
        controls4.update_bullets(screen,  enemies, bullets)
        controls4.update_enemies(stats, screen, gun, enemies, bullets)

def run5():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("PUSHKA-XLOPUSHKA")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls5.create_army(screen, enemies)
    stats = Stats()

    while True:
        controls5.events(screen, gun, bullets)
        gun.update_gun()
        controls5.update(bg_color, screen, gun, enemies, bullets)
        controls5.update_bullets(screen,  enemies, bullets)
        controls5.update_enemies(stats, screen, gun, enemies, bullets)
