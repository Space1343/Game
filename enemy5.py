import pygame

#pygame.mixer.init()
#pygame.mixer.music.load("kosil.mp3")
#pygame.mixer.music.play(-1)

class Enemy5(pygame.sprite.Sprite):
    """Один пртивник"""

    def __init__(self, screen):
        """Загркузка и позиция противников"""
        super(Enemy5, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('cop.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Вывод противника на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещение противников"""
        self.y += 0.095
        self.rect.y = self.y
