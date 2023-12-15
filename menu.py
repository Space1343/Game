import pygame as p
import sys as s

from main import run1
from main import run2
from main import run3
from main import run4
from main import run5

p.init()
screen = p.display.set_mode((800, 600))
p.display.set_caption("PUSHKA-XLOPUSHKA")
bg_color = (255, 255, 255)
fps = 30
clock = p.time.Clock()

def menu():
    global screen
    y = 100
    up = False
    down = True
    list_of_level = []
    f1 = p.font.SysFont('serif', 48)
    text_level1 = f1.render("Level 1", False, (0, 180, 0))

    f2 = p.font.SysFont('serif', 48)
    text_level2 = f2.render("Level 2", False, (0, 180, 0))

    f3 = p.font.SysFont('serif', 48)
    text_level3 = f3.render("Level 3", False, (0, 180, 0))

    f4 = p.font.SysFont('serif', 48)
    text_level4 = f4.render("Level 4", False, (0, 180, 0))

    f5 = p.font.SysFont('serif', 48)
    text_level5 = f5.render("Level 5", False, (0, 180, 0))
    list_of_level.append(text_level1)
    list_of_level.append(text_level2)
    list_of_level.append(text_level3)
    list_of_level.append(text_level4)
    list_of_level.append(text_level5)
    c = 0
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                s.exit()
            elif event.type == p.KEYDOWN:
                if event.key == p.K_UP and up:
                    y -= 100
                if event.key == p.K_DOWN and down:
                    y += 100
                if event.key == p.K_RETURN and y == 100 and level_is_1:
                    p.mixer.init()
                    p.mixer.music.load("fon.mp3")
                    p.mixer.music.play(-1)
                    run1()
                    break
                if event.key == p.K_RETURN and y == 200 and level_is_2:
                    p.mixer.init()
                    p.mixer.music.load("fon.mp3")
                    p.mixer.music.play(-1)
                    run2()
                    break
                if event.key == p.K_RETURN and y == 300 and level_is_3:
                    p.mixer.init()
                    p.mixer.music.load("fon.mp3")
                    p.mixer.music.play(-1)
                    run3()
                    break
                if event.key == p.K_RETURN and y == 400 and level_is_4:
                    p.mixer.init()
                    p.mixer.music.load("fon.mp3")
                    p.mixer.music.play(-1)
                    run4()
                    break
                if event.key == p.K_RETURN and y == 500 and level_is_5:
                    p.mixer.init()
                    p.mixer.music.load("kosil.mp3")
                    p.mixer.music.play(-1)
                    run5()
                    break
        if y == 100:
            up = False
            level_is_1 = True
        if y == 200:
            level_is_2 = True
        if y == 300:
            level_is_3 = True
        if y == 400:
            level_is_4 = True
        elif y == 500:
            down = False
            level_is_5 = True
        else:
            up = True
            down = True
            c = 0
        y_t = 0
        for i in list_of_level:
            y_t += 100
            screen.blit(i, (400, y_t))
        p.draw.rect(screen, (25, 146, 132), (200, y, 100, 75))
        p.display.flip()
        clock.tick(fps)
        screen.fill((100, 100, 100))


if __name__ == "__main__":
    menu()